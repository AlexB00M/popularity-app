from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_user_popularity_task 
from core.apps.items.starGift.models import UserStarGift



@receiver([post_save, post_delete], sender=UserStarGift)
def update_user_popularity_from_gift(sender, instance, **kwargs):
    update_user_popularity_task.delay(instance.user.telegram_id)