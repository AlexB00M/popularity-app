from django.contrib import admin
from .models import GiftLog 

# Register your models here.
@admin.register(GiftLog)
class GiftLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'text', 'star_gift', 'star_gift_unique', 'user_star_gift', 'user_star_gift_unique')
    list_filter = ('id', 'timestamp', 'text', 'star_gift', 'star_gift_unique', 'user_star_gift', 'user_star_gift_unique')
    search_fields = ('id', 'timestamp', 'text', 'star_gift', 'star_gift_unique', 'user_star_gift', 'user_star_gift_unique')