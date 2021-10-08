from django.db import models

# Create your models here.
# User name, email, message and the time message is sent.  


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['timestamp']
