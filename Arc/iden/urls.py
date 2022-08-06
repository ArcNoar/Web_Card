from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'Main'),
    path('skills/', views.skills, name= 'Skills'),
    path('general/', views.general, name= 'General'),
    path('Admin/', views.Admin, name= 'Admin'),
    path('About/', views.About, name= 'About'),
    path('Login/', views.Login, name= 'Login'),

    ]


handler404 = views.pageNotFound