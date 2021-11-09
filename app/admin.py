from django.contrib import admin
from .models import Note
from .models import Task
from .models import Content
from .models import Music

admin.site.register(Note)
admin.site.register(Task)
admin.site.register(Content)
admin.site.register(Music)
