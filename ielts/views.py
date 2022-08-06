from django.shortcuts import render
from .models import writingtask1
# Create your views here.


def home(request):
    return render(request, 'home.html')


def task1categories(request):
    list = writingtask1.objects.all()
    return render(request, 'task1category.html',
                  {'list': list})


def task1list(request, task1type):
    list = writingtask1.objects.filter(type_task=task1type)
    return render(request, 'task1list.html',
                  {'list': list}
                  )
