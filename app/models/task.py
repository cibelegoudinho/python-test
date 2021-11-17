from django.conf import settings
from django.db import models
from django.utils import timezone
from mysite.models import BaseModel

class Task(BaseModel):
    task_title = models.CharField(max_length=200)
    description = models.TextField()
    end_date = models.DateTimeField(default=timezone.now)
    is_completed: models.BooleanField(default=False)

    def __str__(self):
        return self.task_title

