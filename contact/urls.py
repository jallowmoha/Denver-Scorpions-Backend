from django.urls import path
from .views import ContactList, ContactDetail
from django.contrib import admin


urlpatterns = [
    path('contact', ContactList.as_view(), name="contact_list"),
    path('contact/<int:pk>/', ContactDetail.as_view()),
]

admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'