import time

import redis

from hestia.bool_utils import to_bool

from django.db import InterfaceError, OperationalError, ProgrammingError

import conf

from db.models.clusters import Cluster
from db.models.nodes import ClusterNode
from libs.base_monitor import BaseMonitorCommand
from monitor_resources import monitor
from options.registry.k8s import K8S_NODE_NAME


class Command(BaseMonitorCommand):
    help = 'Watch jobs/containers resources.'

    @staticmethod
    def get_node():
        cluster = Cluster.load()
        node = ClusterNode.objects.filter(cluster=cluster, name=conf.get(K8S_NODE_NAME))
        if node.exists():
            return node.first()
        return None

    def get_node_or_wait(self, sleep_interval):
        max_trials = 10
        trials = 0
        while trials < max_trials:
            try:
                return self.get_node()
            except (InterfaceError, ProgrammingError, OperationalError) as e:
                monitor.logger.exception("Database is not synced yet %s\n", e)
                trials += 1
                time.sleep(sleep_interval * 2)
        return None

    def handle(self, *args, **options):
        sleep_interval = options['sleep_interval']
        persist = to_bool(options['persist'])
        node = self.get_node_or_wait(sleep_interval)
        self.stdout.write(
            "Started a new resources monitor with, "
            "log sleep interval: `{}` and persist: `{}`".format(sleep_interval, persist),
            ending='\n')
        containers = {}
        while True:
            try:
                if node:
                    monitor.run(containers, node, persist)
            except redis.exceptions.ConnectionError as e:
                monitor.logger.warning("Redis connection is probably already closed %s\n", e)
            except Exception as e:
                monitor.logger.exception("Unhandled exception occurred %s\n", e)

            time.sleep(sleep_interval)
            try:
                if node:
                    node.refresh_from_db()
                else:
                    node = self.get_node()
            except (InterfaceError, ProgrammingError, OperationalError) as e:
                monitor.logger.exception("Database connection is probably already closed %s\n", e)
                return
