from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listOfAllNotes, name="note.list"),
    path('list/<int:pk>', views.noteDetail, name="note.detail"),

    # USUNG CLASS BASE
    # path('list/', views.NotesListView.as_view()),
    # path('list/<int:pk>', views.NoteDetailView.as_view()),
]
