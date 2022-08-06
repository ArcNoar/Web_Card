from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound



def index(request):
    return render(request, 'iden/Main_Page.html', {'title' : 'Hall'})

def About(request):
    return render(request, 'iden/About.html', {'title' : 'Досье'})

def Admin(request):
    return render(request, 'iden/Admin.html', {'title' : 'Афелий'})

def Login(request):
    return render(request, 'iden/Login.html', {'title' : 'Авторизация'})

def skills(request):
    return HttpResponse('skills')

def general(request):
    return HttpResponse('general')




def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1> Че хател, зачем пришел. </h1>')