from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_user_popularity_task
from core.apps.items.starGiftUnique.models import UserStarGiftUnique


@receiver([post_save, post_delete], sender=UserStarGiftUnique)
def update_user_popularity_from_unique(sender, instance, **kwargs):
    update_user_popularity_task.delay(instance.user.telegram_id)