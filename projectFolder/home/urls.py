from django.urls import path
from . import views

urlpatterns = [
    path('welcome/',views.welcome, name='home.welcome'),
    # path('login/',views.LoginInterfaceView.as_view(), name='login'),
    # path('logout/',views.LogoutInterfaceView.as_view(), name='logout'),
    # path('signup/',views.SignUpView.as_view(), name='registration'),
]
