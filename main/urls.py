from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('projects', views.projects, name = 'projects'),
]