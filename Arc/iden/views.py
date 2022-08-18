from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import UserRegForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='Login')
def index(request):
    return render(request, 'iden/Main_Page.html', {'title' : 'Hall'})

def About(request):
    return render(request, 'iden/About.html', {'title' : 'Досье'})

def Admin(request):
    return render(request, 'iden/Admin.html', {'title' : 'Афелий'})

def Register(request):
    if request.user.is_authenticated:
        return redirect('Main')
    
    else:
        form = UserRegForm
        if request.method == 'POST':
            form = UserRegForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('Login')

        context = {'form':form}
        return render(request, 'iden/Register.html', context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('Main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Main')
            else:
                messages.info(request, 'Username OR Password is incorrect')
                
        context = {}
        return render(request, 'iden/Login.html', context )

def User_LogOut(request):
    logout(request)
    return redirect('Login')



def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1> Че хател, зачем пришел. </h1>')