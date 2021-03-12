from django.db import models


class Audiobook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField(min_value=1)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
