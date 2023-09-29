from django.urls import path
from . import views
# urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('index2',views.index2,name='index2'),
    path('about',views.about,name='about'),
    path('safety',views.safety,name='safety'),
    path('gallery',views.gallery,name='gallery'),
    path('chatbot',views.chatbot,name='chatbot'),
    path('login',views.login,name='login'),
    path('services',views.services,name='services'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('faqs',views.faqs,name='faqs'),
    path('contact_us', views.contact_us,name='contact_us'),
]


# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
