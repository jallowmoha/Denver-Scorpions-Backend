from django.contrib import admin
from .models import Game
# Register your models here.


@admin.register(Game)
class GameModel(admin.ModelAdmin):
    list_display = ('home_team', 'away_team')
    list_filter = ('home_team', 'date_created')

