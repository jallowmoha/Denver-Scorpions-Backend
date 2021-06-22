from django.urls import path
from .views import PlayerList, PlayerDetail
from django.contrib import admin

urlpatterns = [
    path('player/', PlayerList.as_view(), name="player_list"),
    path('player/<int:pk>/', PlayerDetail.as_view()),
]

admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'