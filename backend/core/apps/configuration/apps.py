from django.apps import AppConfig


class ConfgigurationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.configuration'

    def ready(self):
        import core.apps.configuration.signals