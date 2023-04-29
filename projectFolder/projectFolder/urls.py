from django.contrib import admin
from django.urls import path, include
from home.urls import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.welcome, name='welcome'),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('logout/' ,views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup/' ,views.SignUpView.as_view(), name='signup'),
    path('home/', include('home.urls')),
    path('note/', include('note.urls')),

]
