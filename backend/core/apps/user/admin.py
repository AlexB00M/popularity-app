from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('user_name', 'total_popularity', 'telegram_id', 'is_staff', 'is_superuser')
    search_fields = ('telegram_id', 'user_name')
    ordering = ('telegram_id',)

    fieldsets = (
        (None, {'fields': ('telegram_id', 'password')}),
        ('Личная информация', {
            'fields': ('user_name', 'first_name', 'last_name', 'photo_url')
        }),
        ('Связи', {
            'fields': ('friends', 'referals')
        }),
        ('Права доступа', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telegram_id', 'user_name', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions', 'friends', 'referals')
