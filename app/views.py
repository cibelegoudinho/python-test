from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, TemplateView, DetailView, ListView
from django.utils import timezone
from django.db.models import Q
from .models import Note
from .models import Task
from .models import Content
from .models import Music
from .forms import NoteForm
from .forms import TaskForm
from .forms import ContentForm
from .forms import MusicForm
from .functions import get_contents
    
class Home(LoginRequiredMixin, TemplateView):
    template_name = 'app/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contents = Content.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'file_name')
        musics = Music.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'song_title')
        tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'task_title', 'end_date')

        context['contents'] = contents
        context['musics'] = musics
        context['tasks'] = tasks

        return context

    # def dispatch(self, request, *args, **kwargs):
    #     super().dispatch(request, *args, **kwargs)
    #     contents = Content.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'file_name')
    #     musics = Music.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'song_title')
    #     tasks = Task.objects.filter(created_at__lte=timezone.now()).order_by('created_at').values('pk', 'task_title', 'end_date')

    #     response = {
    #         "contents": contents,
    #         "musics": musics,
    #         "tasks": tasks,
    #     }
    #     return render(request, 'app/home.html', response)


class SearchResultsView(TemplateView):
    template_name = 'app/search_results.html'

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        contents = Content.objects.filter(Q(file_name__icontains=query)).values('pk','file_name')
        musics = Music.objects.filter(Q(song_title__icontains=query) | Q(author__icontains=query)).values('pk','song_title', 'author')
        tasks = Task.objects.filter(Q(task_title__icontains=query) | Q(end_date__icontains=query)).values('pk','task_title', 'end_date')

        context['contents'] = contents
        context['musics'] = musics
        context['tasks'] = tasks

        return context


class NoteAll(LoginRequiredMixin, TemplateView):
    template_name = 'app/note/note_all.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = Note.objects.all()
        context['notes'] = notes

        return context

class NoteList(LoginRequiredMixin, TemplateView):
    template_name = 'app/note/note_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notes = Note.objects.all()
        context['notes'] = notes

        return context

class NoteDetail(LoginRequiredMixin, DetailView):
    template_name = 'app/note/note_detail.html'
    model = Note
    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

class NoteCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/note/note_edit.html"
    form_class = NoteForm
    model = Note

    def get_success_url(self):
        return reverse("note_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NoteCreateView, self).form_valid(form)

class NoteUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/note/note_edit.html"
    form_class = NoteForm
    model = Note

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse("note_detail", kwargs={"pk": self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskAll(LoginRequiredMixin, TemplateView):
    template_name = 'app/task/task_all.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks

        return context

class TaskList(LoginRequiredMixin, TemplateView):
    template_name = 'app/task/task_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks = Task.objects.all()
        context['tasks'] = tasks

        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    template_name = 'app/task/task_detail.html'
    model = Task
    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/task/task_edit.html"
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/task/task_edit.html"
    form_class = TaskForm
    model = Task

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ContentAll(LoginRequiredMixin, TemplateView):
    template_name = 'app/content/content_all.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contents = Content.objects.all()
        context['contents'] = contents

        return context

class ContentList(LoginRequiredMixin, TemplateView):
    template_name = 'app/content/content_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        contents = Content.objects.all()
        context['contents'] = contents

        return context

class ContentDetail(LoginRequiredMixin, DetailView):
    template_name = 'app/content/content_detail.html'
    model = Content
    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

class ContentCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/content/content_edit.html"
    form_class = ContentForm
    model = Content

    def get_success_url(self):
        return reverse("content_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ContentCreateView, self).form_valid(form)

class ContentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/content/content_edit.html"
    form_class = ContentForm
    model = Content

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse("content_detail", kwargs={"pk": self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class MusicAll(LoginRequiredMixin, TemplateView):
    template_name = 'app/music/music_all.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        musics = Music.objects.all()
        context['musics'] = musics

        return context

class MusicList(LoginRequiredMixin, TemplateView):
    template_name = 'app/music/music_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        musics = Music.objects.all()
        context['musics'] = musics

        return context

class MusicDetail(LoginRequiredMixin, DetailView):
    template_name = 'app/music/music_detail.html'
    model = Music
    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

class MusicCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/music/music_edit.html"
    form_class = MusicForm
    model = Music

    def get_success_url(self):
        return reverse("music_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(MusicCreateView, self).form_valid(form)

class MusicUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "app/music/music_edit.html"
    form_class = MusicForm
    model = Music

    def get_queryset(self):
        return self.model.objects.filter(pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse("music_detail", kwargs={"pk": self.kwargs.get('pk')})

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)