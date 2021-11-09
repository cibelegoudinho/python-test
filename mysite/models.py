from django.conf import settings
from django.db import models
from django.utils import timezone
2
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, editable=False)
    created_by: models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_by: models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at: models.DateTimeField(auto_now=True, editable=False)
    is_active: models.BooleanField(default=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)