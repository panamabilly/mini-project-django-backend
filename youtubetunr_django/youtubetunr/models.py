from django.db import models


class Youtuber(models.Model):
    name = models.CharField(max_length=100)
    video_title = models.CharField(max_length=200)
    video_url = models.TextField()

    def __str__(self):
        return self.name
