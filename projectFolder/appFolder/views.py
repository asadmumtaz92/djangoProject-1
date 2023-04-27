from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# my first function for testing
# @login_required(login_url=('/admin'))
def home(request):
    return HttpResponse('<h2 style="text-align:center">This is my home page.</h2> <h2 style="text-align:center">Let start to make fun :-)</h2>')

def welcome(request):
    return render(request, 'appFolder/welcome.html', {'today': datetime.today})

@login_required(login_url=('/admin'))
def auth(request):
    return render(request, 'appFolder/auth.html', {})
