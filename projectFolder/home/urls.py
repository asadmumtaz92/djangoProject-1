from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome, name='home.welcome'),
    path('login/',views.LoginInterfaceView.as_view(), name='home.login'),
    path('logout/',views.LogoutInterfaceView.as_view(), name='home.logout'),
    path('signup/',views.SignUpView.as_view(), name='home.signup'),
]
