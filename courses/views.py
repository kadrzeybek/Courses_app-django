from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse('courses')

def details(request):
    return HttpResponse('course details')



def categoryCourse(request,category):
    if(category =='web-programing'):
        text = 'Web Program course list'
    elif(category=='mobil-programing'):
        text = 'Mobil App Program course list'
    else:
        text = 'do not match anything'

    return HttpResponse(f'{text}')