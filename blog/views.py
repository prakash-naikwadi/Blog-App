from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>This is Home Page of Blog</h1>')
def contact(request):
    return HttpResponse('This is Contact Page I am Prakash')