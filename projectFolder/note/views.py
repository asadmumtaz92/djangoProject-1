from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.
from .models import Notes

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
