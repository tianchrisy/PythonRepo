from django.shortcuts import render, HttpResponse
from .models import TodoItem, Item

# Create your views here.
def home(request):
    return render(request, 'home.html')
def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": items})
def aboutus(request):
    return render(request, 'aboutus.html')