from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listOfAllNotes),
    path('list/<int:pk>', views.noteDetail),
]
