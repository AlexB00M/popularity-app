from django.contrib import admin
from .models import Roulette, RouletteSpin

@admin.register(Roulette)
class RouletteAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    
@admin.register(RouletteSpin)
class RouletteSpinAdmin(admin.ModelAdmin):
    list_display = ('user', 'roulette', 'timestamp', 'prize_card', 'prize_gift')
    list_filter = ('user', 'roulette', 'timestamp')
    search_fields = ('user', 'roulette', 'timestamp')
