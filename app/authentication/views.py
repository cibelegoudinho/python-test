from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .forms import CustomUserCreationForm

class UserCreateView(CreateView):
    template_name = "app/cadastro.html"
    form_class = CustomUserCreationForm
    model = User
    
    def get_success_url(self):
        return reverse("home")