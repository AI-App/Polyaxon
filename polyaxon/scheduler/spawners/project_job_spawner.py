import conf

from constants.k8s_jobs import JOB_NAME_FORMAT
from polyaxon_k8s.manager import K8SManager


class ProjectJobSpawner(K8SManager):

    def __init__(self,
                 project_name,
                 project_uuid,
                 job_name,
                 job_uuid,
                 k8s_config=None,
                 namespace='default',
                 in_cluster=False):
        self.project_name = project_name
        self.project_uuid = project_uuid
        self.job_name = job_name
        self.job_uuid = job_uuid

        super().__init__(k8s_config=k8s_config,
                         namespace=namespace,
                         in_cluster=in_cluster)

    @staticmethod
    def _get_proxy_url(namespace, job_name, deployment_name, port):
        return '/{}/proxy/{}.{}.svc.{}:{}'.format(
            job_name,
            deployment_name,
            namespace,
            conf.get('DNS_CUSTOM_CLUSTER'),
            port)

    def _get_service_url(self, job_name):
        deployment_name = JOB_NAME_FORMAT.format(name=job_name, job_uuid=self.job_uuid)
        service = self.get_service(deployment_name)
        if service:
            return self._get_proxy_url(
                namespace=self.namespace,
                job_name=job_name,
                deployment_name=deployment_name,
                port=service.spec.ports[0].port)
        return None

    @staticmethod
    def _get_service_type():
        if conf.get('PUBLIC_PLUGIN_JOBS'):
            return None if conf.get('K8S_INGRESS_ENABLED') else 'LoadBalancer'
        return None

    @staticmethod
    def _use_ingress():
        return conf.get('K8S_INGRESS_ENABLED') and conf.get('PUBLIC_PLUGIN_JOBS')
