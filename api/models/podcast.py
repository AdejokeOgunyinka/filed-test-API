from django.db import models
from django.contrib.postgres.fields import ArrayField


class Podcast(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField(min_value=1)
    upload_time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=100)
    participants = ArrayField(models.CharField(max_length=100))

    def __str__(self):
        return self.name
