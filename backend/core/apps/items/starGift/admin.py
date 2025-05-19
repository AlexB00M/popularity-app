from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import StarGift, UserStarGift
import requests
from django.contrib import messages
from django.conf import settings

@admin.action(description="Update telegram StarGifts")
def update_telegram_gifts(modeladmin, request, queryset):
    user = request.user
    response = requests.get(f'{settings.TELEGRAM_API_URL}/user_gifts/pambolovl', headers=settings.TELEGRAM_API_HEADERS)
    if response.status_code == 200:
        messages.success(request, f"Данные для {user} успешно обновлены.")
    else:
        messages.error(request, f"Ошибка при обновлении {user}: {response.text}")

@admin.register(StarGift)
class StarGiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity_add', 'price', 'drop_chance')
    list_filter = ('name',)
    search_fields = ('name',)
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }
    actions = [update_telegram_gifts]
    
@admin.register(UserStarGift)
class UserStarGiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'star_gift', 'received_date', 'get_from_app', 'sender_id')
    list_filter = ('user',)
    search_fields = ('user__user_name', 'gift__name')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }