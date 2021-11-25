from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from .authentication import views as authentication_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),

    path('signup/', authentication_views.UserCreateView.as_view(), name='sign_up'),

    path('search/', views.SearchResultsView.as_view(), name='search_results'),

    path('', views.Home.as_view(), name='home'), 
    path('note', views.NoteList.as_view(), name='note_list'),
    path('note_all', views.NoteAll.as_view(), name='note_all'),
    path('note/<int:pk>/', views.NoteDetail.as_view(), name='note_detail'),
    path('note/new/', views.NoteCreateView.as_view(), name='note_new'),
    path('note/<int:pk>/edit/', views.NoteUpdateView.as_view(), name='note_edit'),
   
    path('task', views.TaskList.as_view(), name='task_list'),
    path('task_all', views.TaskAll.as_view(), name='task_all'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/new/', views.TaskCreateView.as_view(), name='task_new'),
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view, name='task_edit'),

    path('content', views.ContentList.as_view(), name='content_list'),
    path('content_all', views.ContentAll.as_view(), name='content_all'),
    path('content/<int:pk>/', views.ContentDetail.as_view(), name='content_detail'),
    path('content/new/', views.ContentCreateView.as_view(), name='content_new'), 
    path('content/<int:pk>/edit/', views.ContentUpdateView.as_view(), name='content_edit'),

    path('music_all', views.MusicAll.as_view(), name='music_all'),
    path('music', views.MusicList.as_view(), name='music_list'),
    path('music/<int:pk>/', views.MusicDetail.as_view(), name='music_detail'),
    path('music/new/', views.MusicCreateView.as_view(), name='music_new'),
    path('music/<int:pk>/edit/', views.MusicUpdateView.as_view(), name='music_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)