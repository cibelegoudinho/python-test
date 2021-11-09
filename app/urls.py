from django.urls import path
from . import views

urlpatterns = [
    # path('', views.task_filtered, name='home'), 
    path('', views.music_filtered, name='home'), 
    # path('', views.content_filtered, name='home'), 
    # views.content_filtered, views.music_filtered, 
    path('note', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_new, name='note_new'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('task', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/new/', views.task_new, name='task_new'),
    path('task/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('content', views.content_list, name='content_list'),
    path('content/<int:pk>/', views.content_detail, name='content_detail'),
    path('content/new/', views.content_new, name='content_new'),
    path('content/<int:pk>/edit/', views.content_edit, name='content_edit'),
    path('music', views.music_list, name='music_list'),
    path('music/<int:pk>/', views.music_detail, name='music_detail'),
    path('music/new/', views.music_new, name='music_new'),
    path('music/<int:pk>/edit/', views.music_edit, name='music_edit'),
]