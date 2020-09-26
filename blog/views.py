from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Have to write cbv instead of fbv')
def contact(request):
    return HttpResponse('This is Home Page')