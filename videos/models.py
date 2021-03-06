from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Serie(models.Model):
    name = models.CharField(max_length=99)
    friendly_name = models.CharField(max_length=99, null=True, blank=True)
    genre = models.CharField(max_length=99)
    episodes_count = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Episode(models.Model):
    name = models.CharField(max_length=99)
    friendly_name = models.CharField(max_length=99, null=True, blank=True)
    series = models.ForeignKey('Serie', null=True, blank=True, on_delete=models.SET_NULL)
    video_url = models.URLField(max_length=1024)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class SerieComments(models.Model):
    name = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Serie = models.ForeignKey('Serie', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1024, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    