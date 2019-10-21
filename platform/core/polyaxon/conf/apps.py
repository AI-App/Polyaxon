from django.apps import AppConfig


class ConfConfig(AppConfig):
    name = 'conf'
    verbose_name = 'Conf'

    def ready(self):
        from polyaxon.config_manager import config

        config.setup_conf_service()
