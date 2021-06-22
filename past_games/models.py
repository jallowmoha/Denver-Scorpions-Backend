from django.db import models
from django.core.files.storage import FileSystemStorage as Fs

# Create your models here.


class PastGames(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    home_team = models.CharField(max_length=30, blank=False, default="")
    away_team = models.CharField(max_length=30, blank=False, default="")
    home_logo = models.ImageField(storage=Fs, default="")
    away_logo = models.ImageField(storage=Fs, default="")
    home_team_goals = models.IntegerField(default="")
    away_team_goals = models.IntegerField(default="")

    def __str__(self):
        return self.home_team

    class Meta:
        ordering = ['date_created']
