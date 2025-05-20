from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_user_popularity_task
from .models import UserStarGiftUnique, StarGiftUnique
from core.apps.user.services import calculate_user_popularity  
from core.apps.configuration.models import PopularityConfig

@receiver([post_save, post_delete], sender=UserStarGiftUnique)
def update_user_popularity_from_unique(sender, instance, **kwargs):
    update_user_popularity_task.delay(instance.user.telegram_id)

@receiver(post_save, sender=UserStarGiftUnique)
def recalculate_popularity_add(sender, instance, created, **kwargs):
    if hasattr(instance, '_popularity_updated'):
        return 

    if created or instance._state.adding is False:
        config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')
        instance.popularity_add = config.popularity_per_star * instance.average_price
        instance.save(update_fields=["popularity_add"])
        update_user_popularity_task.delay(instance.user.telegram_id)

        instance._popularity_updated = True