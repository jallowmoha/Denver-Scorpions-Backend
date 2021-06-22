from django.urls import path
from .views import PastGamesList, PastGamesDetail
from django.contrib import admin

urlpatterns = [
    path('pastgames/', PastGamesList.as_view(), name="past_games"),
    path('pastgames/<int:pk>/', PastGamesDetail.as_view()),

]

admin.site.site_header = 'Denver Scorpions'
admin.site.site_title = 'Denver Scorpions'
