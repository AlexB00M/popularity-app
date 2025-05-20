from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_user_popularity_task 
from .models import UserStarGift, StarGift
from core.apps.user.services import calculate_user_popularity  
from core.apps.configuration.models import PopularityConfig

@receiver([post_save, post_delete], sender=UserStarGift)
def update_user_popularity_from_gift(sender, instance, **kwargs):
    update_user_popularity_task.delay(instance.user.telegram_id)

@receiver(post_save, sender=StarGift)
def recalculate_popularity_add(sender, instance, created, **kwargs):
    if getattr(instance, '_popularity_updated', False):
        return

    if created or instance._state.adding is False:
        config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')
        instance.popularity_add = config.popularity_per_star * instance.price
        instance._popularity_updated = True

        instance.save(update_fields=["popularity_add"])

        users = [usg.user for usg in instance.users.select_related("user")]

        for user in users:
            update_user_popularity_task.delay(user.telegram_id)
