from django import forms
from .models import Note
from .models import Task
from .models import Content
from .models import Music
from django.contrib.auth.models import User 

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title', 'text',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('task_title', 'description', 'end_date')

class ContentForm(forms.ModelForm):
    content_file = forms.FileField(required=True)
    class Meta:
        model = Content
        fields = ('file_name', 'content_file')

class MusicForm(forms.ModelForm):

    class Meta:
        model = Music
        fields = ('song_title', 'author')
