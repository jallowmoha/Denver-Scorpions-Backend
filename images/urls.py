from django.urls import path
from .views import ImageList, ImageDetail
from django.contrib import admin

urlpatterns = [
    path('images', ImageList.as_view(), name='image_list'),
    path('images/<int:pk>/', ImageDetail.as_view())
]


admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'