from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listOfAllNotes),
    path('list/<int:pk>', views.noteDetail),

    # USUNG CLASS BASE
    # path('list/', views.NotesListView.as_view()),
    # path('list/<int:pk>', views.NoteDetailView.as_view()),
]
