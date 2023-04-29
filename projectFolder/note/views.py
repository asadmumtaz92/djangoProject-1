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

# =============== START NOTE LIST ===============
def listOfAllNotes(request):
    allNotes = Notes.objects.all()
    return render(request, 'note/noteListView.html', {'allNotes': allNotes})

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "allNotes"
    template_name = 'note/noteListView.html'
    login_url = '/login'

    def get_queryset(self):
        return self.request.user.notes.all()
# =============== END NOTE LIST ===============


# =============== START NOTE DETAIL ===============
def noteDetail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        # raise Http404('Notes dose not exist')
        return HttpResponse('<h1 style="text-align: center; margin-top: 100px">Notes dose not exist</h1>')
    return render(request, 'note/noteDetail.html', {'note': note})

class NoteDetailView(ListView):
    model = Notes
    context_object_name = "note"
    template_name = 'note/noteDetail.html'
# =============== END NOTE DETAIL ===============


# =============== START CREATE NOTE ===============
class NoteCreateView(CreateView):
    model = Notes
    success_url = '/note/list'
    form_class = NoteForm
    template_name = 'note/createNote.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
# =============== END CREATE NOTE ===============


# =============== START UPDATE NOTE ===============
class NoteUpdateView(UpdateView):
    model = Notes
    success_url = '/note/list'
    form_class = NoteForm
    template_name = 'note/noteUpdate.html'
# =============== END UPDATE NOTE ===============


# =============== START DELETE NOTE ===============
class NoteDeleteView(DeleteView):
    model = Notes
    success_url = '/note/list'
    template_name = 'note/noteDelete.html'
# =============== END DELETE NOTE ===============





# def newNote(request):
#     return render(request, 'note/notes_form.html', {})

# def submit(request):
#     print(request)
#     title = request.POST['title']
#     text = request.POST['text']
#     new_note = Notes.objects.create(title=title,text=text)
#     # new_note.save()
#     return HttpResponse(new_note)
