from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Notes
from .forms import NoteForm

def listOfAllNotes(request):
    allNotes = Notes.objects.all()
    return render(request, 'note/noteList.html', {'allNotes': allNotes})


def noteDetail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        # raise Http404('Notes dose not exist')
        return HttpResponse('<h1 style="text-align: center; margin-top: 100px">Notes dose not exist</h1>')
    return render(request, 'note/noteDetail.html', {'note': note})


# def newNote(request):
#     return render(request, 'note/notes_form.html', {})


# USUNG CLASS BASE

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "allNotes"
    template_name = 'note/noteList.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()


# class NoteDetailView(ListView):
#     model = Notes
#     context_object_name = "note"
#     template_name = 'note/noteDetail.html'


class NoteCreateView(CreateView):
    model = Notes
    success_url = '/note/list'
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# def submit(request):
#     print(request)
#     title = request.POST['title']
#     text = request.POST['text']
#     new_note = Notes.objects.create(title=title,text=text)
#     # new_note.save()
#     return HttpResponse(new_note)


class NoteUpdateView(UpdateView):
    model = Notes
    success_url = '/note/list'
    form_class = NoteForm

class NoteDeleteView(DeleteView):
    model = Notes
    success_url = '/note/list'
    # template_name - 'note/noteDelete.html'
