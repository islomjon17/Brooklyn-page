from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def task1categories(request):

    return render(request, 'task1category.html')
