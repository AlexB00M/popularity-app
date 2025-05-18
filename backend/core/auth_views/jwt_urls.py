from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from core.apps.user.views import TelegramTokenView

urlpatterns = [
    path('telegram/', TelegramTokenView.as_view(), name='token_obtain_telegram'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]