from django.db import models
from django.conf import settings

# Create your models here.

class Movie(models.Model):

    title = models.CharField(max_length=20)

    description = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):

    content = models.CharField(max_length=100)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

