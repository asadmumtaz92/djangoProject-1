from django.urls import path
from . import views
# from note.views import *

urlpatterns = [
    path('list/', views.listOfAllNotes, name="note.list"),
    # path('list/', views.NotesListView.as_view(), name="note.list"), # USUNG CLASS BASE

    path('list/<int:pk>', views.noteDetail, name="note.detail"),
    # path('list/<int:pk>', views.NoteDetailView.as_view(), name="note.detail"), # USUNG CLASS BASE

    # path('new/', views.newNote, name="note.new"),
    path('new/', views.NoteCreateView.as_view(), name="note.new"), # USUNG CLASS BASE

    path('edit/<int:pk>', views.NoteUpdateView.as_view(), name="note.update"), # USUNG CLASS BASE

    # path('new_post/', submit, name="note.new_post"),
]
