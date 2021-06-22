from rest_framework import serializers
from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'team_name', 'team_logo', 'match_played', 'matches_won', 'matches_drew', 'matches_lost',
                  'goals_scored', 'goals_conceded', 'points']



