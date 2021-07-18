

from django.db import models


# Create your models here.


class Game(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    home_team = models.CharField(max_length=35, blank=False, default="")
    away_team = models.CharField(max_length=35, blank=False, default="")
    home_logo = models.ImageField(upload_to='images/', default="")
    away_logo = models.ImageField(upload_to='images/', default="")
    game_time = models.DateTimeField()
    game_location = models.CharField(max_length=20, blank=True, default="")

    def __str__(self):
        return self.home_team

    class Meta:
        ordering = ['date_created']
