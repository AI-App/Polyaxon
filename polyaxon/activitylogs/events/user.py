import activitylogs

from events.registry import user

activitylogs.subscribe(user.UserRegisteredEvent)
activitylogs.subscribe(user.UserUpdatedEvent)
activitylogs.subscribe(user.UserActivatedEvent)
activitylogs.subscribe(user.UserDeletedEvent)
activitylogs.subscribe(user.UserGITHUBEvent)
activitylogs.subscribe(user.UserGITLABEvent)
activitylogs.subscribe(user.UserBITBUCKETEvent)
activitylogs.subscribe(user.UserAZUREEvent)
