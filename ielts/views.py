from django.shortcuts import render
from .models import writingtask1, CategoryTask1
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def task1list(request):
    listtask = writingtask1.objects.all
    return render(request, 'task1list.html',
                  {"listtask": listtask}
                  )


def task1show(request, pk):
    listtask = writingtask1.objects.get(pk=pk)
    return render(request, 'task1show.html',
                  {"listtask": listtask}
                  )
