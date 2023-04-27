from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# my first function for testing
# @login_required(login_url=('/admin'))
# def home(request):
#     df = '<h2 style="text-align:center;margin-top:150px;">This is my home page.</h2><h2 style="text-align:center;margin-top:50px;">Let start to make fun :-)</h2>'
#     return HttpResponse(df)


@login_required(login_url=('/admin'))
def welcome(request):
    return render(request, 'home/welcome.html', {'today': datetime.today})


@login_required(login_url=('/admin'))
def auth(request):
    return render(request, 'home/auth.html', {})
