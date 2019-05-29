# pylint:disable=ungrouped-imports

from unittest.mock import patch

import pytest

import auditor

from db.models.clusters import Cluster
from events.registry import cluster as cluster_events
from factories.factory_clusters import ClusterNodeFactory, GPUFactory
from tests.test_auditor.utils import AuditorBaseTest


@pytest.mark.auditor_mark
class AuditorClusterTest(AuditorBaseTest):
    """Testing subscribed events"""
    EVENTS = cluster_events.EVENTS

    def setUp(self):
        self.cluster = Cluster.load()
        self.cluster_node = ClusterNodeFactory(cluster=self.cluster)
        self.node_gpu = GPUFactory(cluster_node=self.cluster_node)
        super().setUp()
        self.tested_events = {
            cluster_events.CLUSTER_CREATED,
            cluster_events.CLUSTER_UPDATED,
            cluster_events.CLUSTER_RESOURCES_UPDATED,
            cluster_events.CLUSTER_NODE_CREATED,
            cluster_events.CLUSTER_NODE_UPDATED,
            cluster_events.CLUSTER_NODE_DELETED,
            cluster_events.CLUSTER_NODE_GPU,
        }

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_created(self,
                             activitylogs_record,
                             tracker_record,
                             notifier_record,
                             executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_CREATED,
                       instance=self.cluster,
                       namespace='test',
                       environment='test',
                       is_upgrade='test',
                       use_data_claim=False,
                       use_outputs_claim=False,
                       use_logs_claim=False,
                       use_repos_claim=False,
                       use_upload_claim=False,
                       node_selector_core_enabled=False,
                       node_selector_experiments_enabled=False,
                       cli_min_version='',
                       cli_latest_version='',
                       platform_min_version='',
                       platform_latest_version='',
                       chart_version='',
                       cpu=0,
                       memory=0,
                       gpu=0)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_updated(self,
                             activitylogs_record,
                             tracker_record,
                             notifier_record,
                             executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_UPDATED,
                       instance=self.cluster,
                       is_upgrade=True)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_resources_updated(self,
                                       activitylogs_record,
                                       tracker_record,
                                       notifier_record,
                                       executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_RESOURCES_UPDATED,
                       instance=self.cluster,
                       n_nodes=0,
                       n_cpus=0,
                       memory=0,
                       n_gpus=0)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_node_created(self,
                                  activitylogs_record,
                                  tracker_record,
                                  notifier_record,
                                  executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_NODE_CREATED,
                       instance=self.cluster_node)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_node_updated(self,
                                  activitylogs_record,
                                  tracker_record,
                                  notifier_record,
                                  executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_NODE_UPDATED,
                       instance=self.cluster_node)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_node_deleted(self,
                                  activitylogs_record,
                                  tracker_record,
                                  notifier_record,
                                  executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_NODE_DELETED,
                       instance=self.cluster_node)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0

    @patch('executor.executor_service.ExecutorService.record_event')
    @patch('notifier.service.NotifierService.record_event')
    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_cluster_node_gpu(self,
                              activitylogs_record,
                              tracker_record,
                              notifier_record,
                              executor_record):
        auditor.record(event_type=cluster_events.CLUSTER_NODE_GPU,
                       instance=self.node_gpu)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 0
        assert notifier_record.call_count == 0
        assert executor_record.call_count == 0


del AuditorBaseTest
