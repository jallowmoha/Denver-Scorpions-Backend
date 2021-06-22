from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'home_team', 'away_team', 'home_logo',  'away_logo', 'game_time', 'game_location']