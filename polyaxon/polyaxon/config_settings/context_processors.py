from polyaxon.config_manager import ROOT_DIR, config

if config.is_monolith_service or config.is_api_service:
    LIST_TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.template.context_processors.debug',
        'django.template.context_processors.media',
        'django.template.context_processors.static',
        'django.template.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'polyaxon.context_processors.versions',
        'polyaxon.context_processors.cluster',
        'api.context_processors.sso_enabled',
    ]

    FRONTEND_DEBUG = config.get_boolean('POLYAXON_FRONTEND_DEBUG')

    if FRONTEND_DEBUG:
        def frontend_debug_processor(request):
            return {'frontend_debug': True}

        LIST_TEMPLATE_CONTEXT_PROCESSORS += ('polyaxon.settings.frontend_debug_processor',)

else:
    LIST_TEMPLATE_CONTEXT_PROCESSORS = [
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'polyaxon.context_processors.versions',
        'polyaxon.context_processors.cluster',
    ]

TEMPLATES_DEBUG = (config.get_boolean('DJANGO_TEMPLATE_DEBUG', is_optional=True) or
                   config.is_debug_mode)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            ROOT_DIR.child('polyaxon').child('polyaxon').child('templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': TEMPLATES_DEBUG,
            'context_processors': LIST_TEMPLATE_CONTEXT_PROCESSORS,
        },
    },
]
