# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('<h1>Django World</h1>')
    return render(request, 'home-todo.html')