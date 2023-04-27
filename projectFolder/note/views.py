from django.shortcuts import render
from django.http import Http404

# Create your views here.
from .models import Notes

def listOfAllNotes(request):
    allNotes = Notes.objects.all()
    return render(request, 'note/note.html', {'allNotes': allNotes})

def noteDetail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404('Notes dose not exist')
    return render(request, 'note/noteDetail.html', {'note': note})
