from django.urls import path, include
from .import views

urlpatterns = [
    
    path('',views.home, name = 'BlogHome'),
    path('contact/',views.contact, name = 'BlogContact'),
]