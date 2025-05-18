from django.contrib import admin
from django_json_widget.widgets import JSONEditorWidget
from .models import SocialLink

@admin.register(SocialLink)
class GiftAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform')
    list_filter = ('user', 'platform')
    search_fields = ('user__user_name', 'platform')
