from django.db.models import Sum, F, FloatField, ExpressionWrapper
from core.apps.user.models import User
from core.apps.items.starGift.models import UserStarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique
from core.apps.configuration.models import PopularityConfig

def calculate_user_popularity(telegram_id):
    user = User.objects.get(telegram_id=telegram_id)
    config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')

    gifts_popularity = UserStarGift.objects.filter(user=user).aggregate(
        total=Sum(
            ExpressionWrapper(
                F('star_gift__price') * config.popularity_per_star,
                output_field=FloatField()
            )
        )
    )['total'] or 0

    unique_gifts_popularity = UserStarGiftUnique.objects.filter(user=user).aggregate(
        total=Sum(
            ExpressionWrapper(
                F('star_gift_unique__average_price') * config.popularity_per_star,
                output_field=FloatField()
            )
        )
    )['total'] or 0
    
    user.total_popularity = gifts_popularity + unique_gifts_popularity
    user.save(update_fields=['total_popularity'])