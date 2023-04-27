from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/', views.home),
    path('welcome/', views.welcome),
    path('auth/', views.auth),
]
