from django.urls import path
from .views import UpdateStarGiftsTelegramAdminView

urlpatterns = [
    path("star-gifts/update/", UpdateStarGiftsTelegramAdminView.as_view(), name="update_telegram_star_gifts")
]