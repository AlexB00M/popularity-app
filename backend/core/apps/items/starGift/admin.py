from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import StarGift, UserStarGift
import requests
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
import json
import zipfile
import io

@admin.action(description="Обновить данные о StarGifts")
def update_telegram_gifts(modeladmin, request, queryset):
    user = request.user
    response = requests.get(f'{settings.TELEGRAM_API_URL}/get_telegram_gifts', headers=settings.TELEGRAM_API_HEADERS)
    if response.status_code == 200:
        for gift in response.json():
            obj, created = StarGift.objects.update_or_create(
                id=gift['id'],
                defaults={
                    'lottie_animation_json': gift['lottie_animation_json']['data'], 
                    'price': gift['price'], 
                    'convert_stars': gift['convert_stars'], 
                    'sold_out': gift['sold_out']
                }
            )
            if created:
                messages.success(request, f"Добавлен новый подарок: {gift['id']}")
        messages.success(request, f"Все данные для успешно обновлены.")
    else:
        messages.error(request, f"Ошибка при обновлении {user}: {response.text}")
        
@admin.action(description="Скачать Lottie JSON")
def export_lottie_json(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Выберите один объект для экспорта.")
        return

    gift = queryset.first()
    json_data = gift.lottie_animation_json
    file_content = json.dumps(json_data, ensure_ascii=False, indent=2)

    response = HttpResponse(file_content, content_type='application/json')
    response['Content-Disposition'] = f'attachment; filename="lottie_{gift.id}.json"'
    return response

import io
import zipfile
import json
from django.http import HttpResponse

@admin.action(description="Скачать JSON-файлы (ZIP)")
def export_multiple_lottie_json(modeladmin, request, queryset):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for gift in queryset:
            file_content = json.dumps(gift.lottie_animation_json, ensure_ascii=False, indent=2)
            filename = f"lottie_{gift.id}.json"
            zip_file.writestr(filename, file_content)

    buffer.seek(0)
    response = HttpResponse(buffer.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="lottie_exports.zip"'
    return response


@admin.register(StarGift)
class StarGiftAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'popularity_add', 'price', 'drop_chance', 'sold_out')
    list_filter = ('name', 'popularity_add', 'price', 'drop_chance', 'sold_out')
    search_fields = ('id', 'name', 'popularity_add', 'price', 'drop_chance', 'sold_out')
    ordering = ['sold_out', 'price']
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }
    actions = [update_telegram_gifts, export_lottie_json, export_multiple_lottie_json]
    
@admin.register(UserStarGift)
class UserStarGiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'star_gift', 'get_star_gift_popularity','received_date', 'get_from_app', 'sender_id')
    list_filter = ('user',)
    search_fields = ('user__user_name', 'gift__name')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }

    def get_star_gift_popularity(self, obj):
        return obj.star_gift.popularity_add

    get_star_gift_popularity.short_description = 'Popularity_add'