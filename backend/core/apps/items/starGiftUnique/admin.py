from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import StarGiftUnique, UserStarGiftUnique

@admin.register(StarGiftUnique)
class StarGiftUniqueAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'popularity_add', 'average_price')
    list_filter = ('title', 'model', 'popularity_add', 'average_price')
    search_fields = ('title', 'model', 'popularity_add', 'average_price')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }
    
@admin.register(UserStarGiftUnique)
class UserStarGiftUniqueAdmin(admin.ModelAdmin):
    list_display = ('user', 'star_gift_unique', 'star_gift_unique__popularity_add', 'received_date', 'get_from_app', 'sender_id')
    list_filter = ('user',)
    search_fields = ('user__user_name', 'star_gift_unique__title', 'star_gift_unique__id')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }