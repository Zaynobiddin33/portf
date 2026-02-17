from functools import wraps
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def requires_task(completed_level):
    """Gate a task view — user must have completed at least this level."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.session.get('completed_task', 0) < completed_level:
                return redirect('task1')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# Create your views here.

def main(request):
     technologies_raw = models.Techs.objects.all()
     technologies = [tech.name for tech in technologies_raw]
     if request.user.is_authenticated:
        context = {
             'messages': models.Messages.objects.all().order_by('-id'),
             'techs': technologies
        }
     else:
        context = {
             'messages': 0,
             'techs': technologies
        }
     return render(request,'portfolio.html', context)

def contact(request):
     sent = False
     if request.method == 'POST':
          email = request.POST['email']
          message = request.POST['message']
          models.Messages.objects.create(
               email = email,
               text = message
          )
          sent = True

     return render(request,'contact.html', {'sent': sent})

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


def task1(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'HELLO':
               request.session['completed_task'] = 1
               return redirect('task2')
          return render(request, 'task/task1.html', {'error': True})
     return render(request, 'task/task1.html')


@requires_task(1)
def task2(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip()
          if answer == '4927':
               request.session['completed_task'] = 2
               return redirect('task3')
          return render(request, 'task/task2.html', {'error': True})
     return render(request, 'task/task2.html')


@requires_task(2)
def task3(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'GHOST':
               request.session['completed_task'] = 3
               return redirect('task4')
          return render(request, 'task/task3.html', {'error': True})
     return render(request, 'task/task3.html')


@requires_task(3)
def task4(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip()
          if answer == '42':
               request.session['completed_task'] = 4
               return redirect('task5')
          return render(request, 'task/task4.html', {'error': True})
     return render(request, 'task/task4.html')


@requires_task(4)
def task5(request):
     request.session['completed_task'] = 5
     return render(request, 'task/task5.html')


@requires_task(5)
def task6(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'CIPHER':
               request.session['completed_task'] = 6
               return redirect('task7')
          return render(request, 'task/task6.html', {'error': True})
     return render(request, 'task/task6.html')


@requires_task(6)
def task7(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'SHADOW':
               request.session['completed_task'] = 7
               return redirect('task8')
          return render(request, 'task/task7.html', {'error': True})
     return render(request, 'task/task7.html')


@requires_task(7)
def task8(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'BINARY':
               request.session['completed_task'] = 8
               return redirect('task9')
          return render(request, 'task/task8.html', {'error': True})
     return render(request, 'task/task8.html')


@requires_task(8)
def task9(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'PHOENIX':
               request.session['completed_task'] = 9
               return redirect('task10')
          response = render(request, 'task/task9.html', {'error': True})
          response['X-Secret'] = 'the answer is PHOENIX'
          return response
     response = render(request, 'task/task9.html')
     response['X-Secret'] = 'the answer is PHOENIX'
     return response


@requires_task(9)
def task10(request):
     if request.method == 'POST':
          answer = request.POST.get('answer', '').strip().upper()
          if answer == 'ECLIPSE':
               request.session['completed_task'] = 10
               return redirect('victory')
          return render(request, 'task/task10.html', {'error': True})
     return render(request, 'task/task10.html')


@requires_task(10)
def victory(request):
     return render(request, 'task/victory.html')