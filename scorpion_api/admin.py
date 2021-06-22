from django.contrib import admin
from .models import Player

# Register your models here.


@admin.register(Player)
class PlayerModel(admin.ModelAdmin):
    list_display = ('name', 'position')
    list_filter = ('name', 'date_created')