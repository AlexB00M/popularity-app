from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User 

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # укажите здесь поля и конфигурацию админки, например:
    list_display = ('telegram_id', 'user_name', 'is_staff', 'is_superuser')
    search_fields = ('telegram_id', 'user_name')
    ordering = ('telegram_id',)

    fieldsets = (
        (None, {'fields': ('telegram_id', 'user_name', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'photo_url')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telegram_id', 'user_name', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')