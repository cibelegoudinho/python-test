from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Note
from .models import Task
from .models import Content
from .models import Music
from .forms import NoteForm
from .forms import TaskForm
from .forms import ContentForm
from .forms import MusicForm

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'app/note_list.html', {'notes': notes})

def note_detail (request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'app/note_detail.html', {'note': note})

def note_new(request):
    if request.method == "POST":
         form = NoteForm(request.POST)
         if form.is_valid():
             note = form.save(commit=False)
             note.user = request.user
             note.save()
             return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'app/note_edit.html', {'form': form})

def note_edit(request, pk):
     note = get_object_or_404(Note, pk=pk)
     if request.method == "POST":
         form = NoteForm(request.POST, instance=note)
         if form.is_valid():
             note = form.save(commit=False)
             note.user = request.user
             note.save()
             return redirect('note_detail', pk=note.pk)
     else:
         form = NoteForm(instance=note)
     return render(request, 'app/note_edit.html', {'form': form})


def task_filtered(request):
    tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at') 
    return render(request, 'app/home.html', {'tasks': tasks})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'app/task_list.html', {'tasks': tasks})

def task_detail (request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'app/task_detail.html', {'task': task})

def task_new(request):
    if request.method == "POST":
         form = TaskForm(request.POST)
         if form.is_valid():
             task = form.save(commit=False)
             task.user = request.user
             task.save()
             return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'app/task_edit.html', {'form': form})

def task_edit(request, pk):
     task = get_object_or_404(Task, pk=pk)
     if request.method == "POST":
         form = TaskForm(request.POST, instance=task)
         if form.is_valid():
             task = form.save(commit=False)
             task.user = request.user
             task.save()
             return redirect('task_detail', pk=task.pk)
     else:
         form = TaskForm(instance=task)
     return render(request, 'app/task_edit.html', {'form': form})


def content_filtered(request):
    contents = Content.objects.filter(created_at__lte=timezone.now()).order_by('created_at') 
    return render(request, 'app/home.html', {'contents': contents})

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'app/content_list.html', {'contents': contents})

def content_detail (request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'app/content_detail.html', {'content': content})

def content_new(request):
    if request.method == "POST":
         form = ContentForm(request.POST)
         if form.is_valid():
             content = form.save(commit=False)
             content.user = request.user
             content.save()
             return redirect('content_detail', pk=content.pk)
    else:
        form = ContentForm()
    return render(request, 'app/content_edit.html', {'form': form})

def content_edit(request, pk):
     content = get_object_or_404(Content, pk=pk)
     if request.method == "POST":
         form = ContentForm(request.POST, instance=content)
         if form.is_valid():
             content = form.save(commit=False)
             content.user = request.user
             content.save()
             return redirect('content_detail', pk=content.pk)
     else:
         form = ContentForm(instance=content)
     return render(request, 'app/content_edit.html', {'form': form})


def music_filtered(request):
    musics = Music.objects.filter(created_at__lte=timezone.now()).order_by('created_at') 
    return render(request, 'app/home.html', {'musics': musics})

def music_list(request):
    musics = Music.objects.all()
    return render(request, 'app/music_list.html', {'musics': musics})

def music_detail (request, pk):
    music = get_object_or_404(Music, pk=pk)
    return render(request, 'app/music_detail.html', {'music': music})

def music_new(request):
    if request.method == "POST":
         form = MusicForm(request.POST)
         if form.is_valid():
             music = form.save(commit=False)
             music.user = request.user
             music.save()
             return redirect('music_detail', pk=music.pk)
    else:
        form = MusicForm()
    return render(request, 'app/music_edit.html', {'form': form})

def music_edit(request, pk):
     music = get_object_or_404(Music, pk=pk)
     if request.method == "POST":
         form = MusicForm(request.POST, instance=music)
         if form.is_valid():
             music = form.save(commit=False)
             music.user = request.user
             music.save()
             return redirect('music_detail', pk=music.pk)
     else:
         form = MusicForm(instance=music)
     return render(request, 'app/music_edit.html', {'form': form})