from django.contrib import admin
from django.urls import path, include
from core.apps.user.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/profile/', ProfileView.as_view(), name='profile_view'),
    path('api/auth/', include('core.auth_views.jwt_urls')),
]
