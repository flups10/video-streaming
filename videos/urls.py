from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_videos, name="videos"),
    path('<serie_id>/', views.current_serie_details,
         name="current_serie_details"),
    path('<comment_id>', views.delete_comment, name="delete_comment"),
    path('<serie_id>/<comment_id>', views.edit_comment, name="edit_comment"),
    path('<serie_id>/<episode_id>/', views.current_episode_details, name="current_episode_details"),
]
