from django.contrib import admin
from .models import Emoji 

# Register your models here.
@admin.register(Emoji)
class EmojiAdmin(admin.ModelAdmin):
    list_display = ('id', 'animated', 'image')
    list_filter = ('animated',)
    search_fields = ('id',)