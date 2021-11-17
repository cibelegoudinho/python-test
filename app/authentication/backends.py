from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db import reset_queries
from django.forms import ValidationError
from django.db.models import Q

User = get_user_model()

class CustomModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            username = user.username
        except User.DoesNotExist:
            return None

        if not user.is_active and user.block_message:
            raise ValidationError(user.block_message, code='inactive')

        res = super().authenticate(request, username, password, **kwargs)
        return res