from django.conf import settings
from django.db import models
from mysite.models import BaseModel


class Note(BaseModel):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

