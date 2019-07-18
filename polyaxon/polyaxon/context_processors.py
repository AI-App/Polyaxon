from db.models.clusters import Cluster
from db.models.versions import ChartVersion, CliVersion, LibVersion, PlatformVersion


def cluster(request):
    return {'cluster': Cluster.load()}


def versions(request):
    return {
        'cli_version': CliVersion.load(),
        'platform_version': PlatformVersion.load(),
        'lib_version': LibVersion.load(),
        'chart_version': ChartVersion.load(),
        'assets_version': '0.5.3'
    }
