from django.contrib import admin
from django.urls import path
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    path('',views.home, name ='home'),
    path('selectLob',views.newgraph, name ='newgraph'),
]
