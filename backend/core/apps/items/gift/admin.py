from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import Gift, UserGift

@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity_add', 'price', 'drop_chance')
    list_filter = ('name',)
    search_fields = ('name',)
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }
    
@admin.register(UserGift)
class UserGiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'gift', 'timestamp', 'get_from_app', 'user_sender')
    list_filter = ('user',)
    search_fields = ('user__user_name', 'gift__name')
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }