from django.conf import settings
from django.db import models
from mysite.models import BaseModel

class Content(BaseModel):
    file_name = models.CharField(max_length=200)
    content_file = models.FileField() 

    def __str__(self):
        return self.file_name

