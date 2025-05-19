from django.apps import AppConfig


class GiftuniqeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.apps.items.starGiftUnique'

    def ready(self):
        import core.apps.items.starGiftUnique.signals