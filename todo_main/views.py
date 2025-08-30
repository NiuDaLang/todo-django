# from django.http import HttpResponse
from django.shortcuts import render
from todo.models import Task

def home(request):
    # return HttpResponse('<h1>Django World</h1>')
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    tasks_completed = Task.objects.filter(is_completed=True)
    context = {
        'tasks': tasks,
        'tasks_completed': tasks_completed,
    }
    return render(request, 'home-todo.html', context)