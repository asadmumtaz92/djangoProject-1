from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/registration.html'
    success_url = '/home/welcome'
    
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home.welcome')
        return super().get(self, request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = '/home/welcome'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    success_url = 'home/welcome.html'


# @login_required(login_url=('/admin'))
def welcome(request):
    return render(request, 'home/welcome.html', {'today': datetime.today})
    # OR
    # df = '<h2 style="text-align:center;margin-top:150px;">This is my home page.</h2><h2 style="text-align:center;margin-top:50px;">Let start to make fun :-)</h2>'
    # return HttpResponse(df)
