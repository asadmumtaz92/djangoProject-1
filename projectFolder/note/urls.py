from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listOfAllNotes),
    path('noteDetail/<int:pk>', views.noteDetail),
]
