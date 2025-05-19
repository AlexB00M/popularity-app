from django.apps import AppConfig


class GiftConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.items.starGift'

    def ready(self):
        import core.apps.items.starGift.signals