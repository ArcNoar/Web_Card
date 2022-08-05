from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')

def skills(request):
    return HttpResponse('skills')

def general(request):
    return HttpResponse('general')
