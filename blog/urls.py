from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name = 'BlogHome'),
    path('contact/',views.contact, name = 'BlogContact'),
    path('about/',views.contact, name = 'about'),
    path('login/', views.login_signup, name='login'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)