from django.db.models import Sum, F, FloatField, ExpressionWrapper
from core.apps.user.models import User
from core.apps.items.starGift.models import UserStarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique


def calculate_user_popularity(telegram_id):
    user = User.objects.get(telegram_id=telegram_id)
    gifts_popularity = UserStarGift.objects.filter(user=user).aggregate(
        total=Sum('star_gift__popularity_add')
    )['total'] or 0

    unique_gifts_popularity = UserStarGiftUnique.objects.filter(user=user).aggregate(
        total=Sum(
            ExpressionWrapper(
                F('star_gift_unique__popularity_add') * F('star_gift_unique__average_price'),
                output_field=FloatField()
            )
        )
    )['total'] or 0

    user.total_popularity = gifts_popularity + unique_gifts_popularity
    user.save(update_fields=['total_popularity'])