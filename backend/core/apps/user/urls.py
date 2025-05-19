from django.urls import path
from .views import LeaderboardView, UserRankView, UserGiftsView

urlpatterns = [
    path('user_gifts/', UserGiftsView.as_view(), name='profile_view'),
    path("leaderboard/<int:page>", LeaderboardView.as_view(), name="leaderboard"),
    path("user_rank/", UserRankView.as_view(), name="user_rank")
]