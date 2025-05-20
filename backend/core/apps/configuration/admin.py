from django.contrib import admin
from .models import PopularityConfig 

# Register your models here.
@admin.register(PopularityConfig)
class PopularityConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'popularity_per_star', 'popularity_per_ton')
    list_filter = ('popularity_per_star', 'popularity_per_ton')
    search_fields = ('popularity_per_star', 'popularity_per_ton')