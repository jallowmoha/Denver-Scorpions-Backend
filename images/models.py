from django.db import models


# Create your models here.


def user_directory_path(instance, filename):
    return 'images/{0}/'.format(filename)


class Images(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    background_img = models.ImageField(upload_to='images/', default="")
    background_alt = models.CharField(max_length=20, blank=False, default="")
    gallery_img = models.ImageField(upload_to='images/', default="")
    gallery_alt = models.CharField(max_length=20, blank=False, default="")

    class Meta:
        ordering = ["date_created"]



