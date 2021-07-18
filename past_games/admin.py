from django.contrib import admin
from .models import PastGames

# Register your models here.


@admin.register(PastGames)
class PastGamesMode(admin.ModelAdmin):
    list_display = ('home_team', 'away_team')
    list_filter = ('home_team', 'away_team')