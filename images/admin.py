from django.contrib import admin
from .models import Images

# Register your models here.


@admin.register(Images)
class ImageModel(admin.ModelAdmin):
    list_display = ('background_alt', "gallery_alt")
    list_filter = ('background_alt', "gallery_alt")