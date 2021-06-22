from django.db import models
from django.core.files.storage import FileSystemStorage as fs

# Create your models here.


class Table(models.Model):
    team_name = models.CharField(max_length=30, blank=False)
    team_logo = models.ImageField(storage=fs, default="")
    match_played = models.IntegerField(default="")
    matches_won = models.IntegerField(default="")
    matches_drew = models.SmallIntegerField(null=True)
    matches_lost = models.IntegerField(default="")
    goals_scored = models.IntegerField(default="")
    goals_conceded = models.IntegerField(default="")
    points = models.IntegerField(default="")


    def __str__(self):
        return self.team_name

