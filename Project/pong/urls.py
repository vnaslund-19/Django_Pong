# pong/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1v1/', views.play_1v1, name='play_1v1'),
    path('AI/', views.play_AI, name='play_AI'),
    path('spectate/', views.spectate, name='spectate'),
]