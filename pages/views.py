from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('homepage')

def contact(request):
    return HttpResponse('contact')

def aboutUs(request):
    return HttpResponse('aboutUs')