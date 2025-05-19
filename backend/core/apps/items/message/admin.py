from django.contrib import admin
from .models import Message 

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message_text')
    list_filter = ('id', 'message_text')
    search_fields = ('id', 'message_text')