from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView

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

# class NotesListView(ListView):
#     model = Notes
#     context_object_name = "allNotes"
#     template_name = 'note/noteList.html'


# class NoteDetailView(ListView):
#     model = Notes
#     context_object_name = "note"
#     template_name = 'note/noteDetail.html'


class NoteCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    success_url = '/note/list'
    form_class = NoteForm


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
