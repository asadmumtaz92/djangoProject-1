from django.contrib import admin
from django.urls import path, include
from home.urls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('home/',include('home.urls')),
    path('note/',include('note.urls')),
]
