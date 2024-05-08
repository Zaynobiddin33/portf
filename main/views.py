from django.shortcuts import render
from . import models


# Create your views here.

def main(request):
    if request.user.is_authenticated:
        context = {
             'messages': models.Messages.objects.all().order_by('-id')
        }
    else:
        context = {
             'messages': 0
        }
        
    return render(request,'portfolio.html', context)

def contact(request):
     if request.method == 'POST':
          email = request.POST['email']
          message = request.POST['message']
          models.Messages.objects.create(
               email = email,
               text = message
          )

     return render(request,'contact.html')

def about(request):
     about_me = models.AboutMe.objects.order_by('-id').first()
     context = {
          'about': about_me
     }
     return render(request,'about.html', context)

def projects(request):
     projects = models.Project.objects.all()
     context = {
          'projects': projects
     }
     return render(request,'projects.html', context)