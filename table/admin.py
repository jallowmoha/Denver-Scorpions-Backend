from django.contrib import admin
from .models import Table

# Register your models here.


@admin.register(Table)
class TableModel(admin.ModelAdmin):
    list_display = ('team_name', 'points')
    list_filter = ('team_name', 'points')
