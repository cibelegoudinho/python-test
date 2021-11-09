from django.conf import settings
from django.db import models
from mysite.models import BaseModel

class Music(BaseModel):
    song_title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.song_title
        