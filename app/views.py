from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Note

def note_list(request):
    notes = Note.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'app/note_list.html', {'notes': notes})


def note_detail (request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'app/note_detail.html', {'note': note})