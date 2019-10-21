import logging

from django_auth_ldap.backend import populate_user

from django.dispatch import receiver

import auditor
import conf

from events.registry.user import USER_LDAP
from options.registry.email import EMAIL_DEFAULT_DOMAIN

_logger = logging.getLogger('polyaxon.users.auth_ldap')


@receiver(populate_user)
def populate_user_handler(sender, **kwargs):
    user = kwargs['user']
    auditor.record(event_type=USER_LDAP)
    ldap_user = user.ldap_user

    # populate user with default email to prevent validation error
    if not user.email:
        try:
            value = ldap_user.attrs['mail'][0]
        except LookupError:
            _logger.error("%s does not have a value for the attribute %s",
                          ldap_user.dn, 'mail',
                          exc_info=True)
            user.email = '%s@%s' % (user.username, conf.get(EMAIL_DEFAULT_DOMAIN))
        else:
            user.email = value
