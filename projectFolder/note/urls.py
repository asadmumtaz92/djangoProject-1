from django.urls import path
from . import views
from note.views import *
urlpatterns = [
    path('list/', views.listOfAllNotes, name="note.list"),
    path('list/<int:pk>', views.noteDetail, name="note.detail"),
    # path('new/', views.newNote, name="note.new"),

    # USUNG CLASS BASE
    # path('list/', views.NotesListView.as_view(), name="note.list"),
    # path('list/<int:pk>', views.NoteDetailView.as_view(), name="note.detail"),
    # path('new/', views.NoteCreateView.as_view(), name="note.new"),
    # path('new_post/', submit, name="note.new_post"),
]
