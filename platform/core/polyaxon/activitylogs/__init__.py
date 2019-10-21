from hestia.service_interface import LazyServiceWrapper

from activitylogs.manager import default_manager
from activitylogs.service import ActivityLogService

backend = LazyServiceWrapper(
    backend_base=ActivityLogService,
    backend_path='activitylogs.service.ActivityLogService',
    options={}
)
backend.expose(locals())

subscribe = default_manager.subscribe
