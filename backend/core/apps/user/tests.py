from django.test import TestCase
from core.apps.user.models import User
from core.apps.items.starGift.models import StarGift, UserStarGift
from core.apps.user.tasks import update_user_popularity_task

class CeleryTaskTestCase(TestCase):
    def test_update_user_popularity_task(self):
        telegram_id = 5000549728

        # Создаём пользователя в тестовой БД
        user = User.objects.create_user(
            telegram_id=telegram_id,
            user_name="TestUser"
        )
        gift = StarGift.objects.create(
            id=1,
            popularity_add=200,
            price=20
        )

        for i in range(20):
            UserStarGift.objects.create(
                user=user,
                star_gift=gift,
            )

        # Передаём именно telegram_id
        print(f"Популярность до: {user.total_popularity}")
        update_user_popularity_task.apply(args=[user.telegram_id])
        # user.refresh_from_db()
        print(f"Популярность после: {user.total_popularity}")
        self.assertEqual(user.total_popularity, 4000)
