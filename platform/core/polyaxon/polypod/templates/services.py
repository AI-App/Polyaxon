from hestia.list_utils import to_list
from kubernetes import client

from polyaxon_k8s import constants as k8s_constants


def get_service(namespace, name, labels, ports, target_ports,
                service_type=None, external_i_ps=None):
    external_i_ps = to_list(external_i_ps) if external_i_ps else None
    ports = to_list(ports)
    metadata = client.V1ObjectMeta(name=name, labels=labels, namespace=namespace)
    service_ports = [client.V1ServicePort(port=port, target_port=target_port) for port, target_port
                     in zip(ports, target_ports)]
    spec = client.V1ServiceSpec(selector=labels,
                                type=service_type,
                                external_i_ps=external_i_ps,
                                ports=service_ports)
    return client.V1Service(api_version=k8s_constants.K8S_API_VERSION_V1,
                            kind=k8s_constants.K8S_SERVICE_KIND,
                            metadata=metadata,
                            spec=spec)
