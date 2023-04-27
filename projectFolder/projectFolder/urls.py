from django.contrib import admin
from django.urls import path, include
from appFolder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('welcome/', views.welcome),
    path('auth/', views.auth),
    path('notes/', include('note.urls')),
]
