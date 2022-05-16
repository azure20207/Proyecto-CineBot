from django.urls import path, include
from .views import UsuarioList
from django.shortcuts import render
from . import views

urlpatterns = [
    path('cinebot/', views.index, name='index'),

    
]





