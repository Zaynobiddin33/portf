from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
    path('projects', views.projects, name = 'projects'),
    path('task/1', views.task1, name='task1'),
    path('task/2', views.task2, name='task2'),
    path('task/3', views.task3, name='task3'),
    path('task/4', views.task4, name='task4'),
    path('task/5', views.task5, name='task5'),
    path('task/6', views.task6, name='task6'),
    path('task/7', views.task7, name='task7'),
    path('task/8', views.task8, name='task8'),
    path('task/9', views.task9, name='task9'),
    path('task/10', views.task10, name='task10'),
    path('task/victory', views.victory, name='victory'),
]
