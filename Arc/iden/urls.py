from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'Main'),
    path('Admin/', views.Admin, name= 'Admin'),
    path('About/', views.About, name= 'About'),
    path('Login/', views.Login, name= 'Login'),
    path('LogOut/', views.User_LogOut, name= 'LogOut'),
    path('Register/', views.Register, name= 'Register'),
    path('Synopsis/', views.Synopsis, name= 'Synopsis'),

    ]


handler404 = views.pageNotFound