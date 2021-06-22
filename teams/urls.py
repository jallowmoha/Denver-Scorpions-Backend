from django.urls import path
from .views import GameList, GameDetail
from django.contrib import admin

urlpatterns = [
    path('game/', GameList.as_view(), name="game_list" ),
    path('game/<int:pk>/', GameDetail.as_view()),


]

admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'