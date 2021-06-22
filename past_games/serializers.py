from rest_framework import serializers
from .models import PastGames

class PastGamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastGames
        fields = ['id', 'home_team', 'away_team', 'home_logo', 'away_logo',
                  'home_team_goals', 'away_team_goals']