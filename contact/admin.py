from django.contrib import admin
from .models import Contact


# Register your models here.


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_display = ('name', 'email')
    list_filter = ('name', 'email')