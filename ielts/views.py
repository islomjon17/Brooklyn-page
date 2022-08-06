from django.shortcuts import render
from .models import writingtask1, CategoryTask1
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'home.html')


def task1categories(request):
    listtask = writingtask1.objects.all()
    listcat = CategoryTask1.objects.all()

    return render(request, 'task1category.html',
                  {"listtask": listtask, "listcat": listcat})


def task1list(request, pk):
    listtask = writingtask1.objects.filter(
        pk=pk)
    return render(request, 'task1list.html',
                  {"listtask": listtask}
                  )
