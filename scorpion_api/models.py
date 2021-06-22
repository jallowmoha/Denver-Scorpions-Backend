from django.db import models
from django.core.files.storage import FileSystemStorage as fs

# Create your models here.


class Player(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length= 30, blank=False, default="")
    position = models.CharField(max_length=30)
    player_number = models.IntegerField(default="")
    photo = models.ImageField(upload_to='images', storage=fs, default="")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_created']