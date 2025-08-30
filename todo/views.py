from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def addTask(request):
  # print(request.POST['task'])
  # return HttpResponse('The form is submitted')
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')