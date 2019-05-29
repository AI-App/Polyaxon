import tracker

from events.registry import user

tracker.subscribe(user.UserRegisteredEvent)
tracker.subscribe(user.UserUpdatedEvent)
tracker.subscribe(user.UserActivatedEvent)
tracker.subscribe(user.UserDeletedEvent)
tracker.subscribe(user.UserLDAPEvent)
tracker.subscribe(user.UserGITHUBEvent)
tracker.subscribe(user.UserGITLABEvent)
tracker.subscribe(user.UserBITBUCKETEvent)
tracker.subscribe(user.UserAZUREEvent)
