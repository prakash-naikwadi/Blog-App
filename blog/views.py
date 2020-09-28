from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'blog/blog_home.html', {})
def contact(request):
    return HttpResponse('This is Http Respose(Manisha) Contact Page')
def about(request):
    return HttpResponse('<h1>This is About Page of Blog</h1>')

def login_signup(request):
    return HttpResponse('<h1>This is login and signup page</h1>')
