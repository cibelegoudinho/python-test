from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Note
from .forms import NoteForm

def note_list(request):
    notes = Note.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
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
             note.published_date = timezone.now()
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
             note.published_date = timezone.now()
             note.save()
             return redirect('note_detail', pk=note.pk)
     else:
         form = NoteForm(instance=note)
     return render(request, 'app/note_edit.html', {'form': form})