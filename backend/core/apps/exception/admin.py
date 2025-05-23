from django.contrib import admin
from .models import LoggedException 

# Register your models here.
@admin.register(LoggedException)
class LoggedExceptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'text')
    list_filter = ('id', 'timestamp', 'text')
    search_fields = ('id', 'timestamp', 'text')