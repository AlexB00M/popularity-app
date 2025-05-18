from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from django.db import models
from .models import Card, UserCard

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity_add', 'price', 'drop_chance')
    search_fields = ('name',)
    list_filter = ('name',)
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget(options={'theme': 'dark'})},
    }
    
@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'card', 'timestamp', 'get_from_app', 'user_sender')
    list_filter = ('user',)
    search_fields = ('user__user_name', 'card__name')