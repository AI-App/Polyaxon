from django.apps import AppConfig


class CronsConfig(AppConfig):
    name = 'crons'
    verbose_name = 'Crons'

    def ready(self):
        import signals.nodes  # noqa
        import signals.deletion  # noqa
