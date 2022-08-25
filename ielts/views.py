from re import L
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView
from .forms import writingtask1Form, writingtask2Form
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
# import pagnations stuff for odf downloader...
from django.core.paginator import Paginator
# Create your views here.


def Home(request):
    return render(request, 'home.html')

# Task 1 section


def Task1list(request):
    listtask = writingtask1.objects.all

    # Set up pagination
    p = Paginator(writingtask1.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)
    nums = "a" * tasks.paginator.num_pages

    return render(request, 'tasks/task1/task1list.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )


def Task1show(request, task1_id):
    listtask = writingtask1.objects.get(pk=task1_id)
    return render(request, 'tasks/task1/task1show.html',
                  {"listtask": listtask}
                  )


class UpdateTask1View(UpdateView):
    model = writingtask1
    form_class = writingtask1Form
    context_object_name = 'post'
    template_name = 'tasks/task1/task1update.html'


class DeleteTask1View(DeleteView):
    model = writingtask1
    template_name = 'tasks/task1/delete_task1.html'
    success_url = reverse_lazy('home')


class AddTaskView(CreateView):
    model = writingtask1
    form_class = writingtask1Form
    template_name = 'tasks/task1/addtask1.html'


# Task 2 section


def Task2list(request):
    listtask = writingtask2.objects.all

    # Set up pagination
    p = Paginator(writingtask2.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)
    nums = "a" * tasks.paginator.num_pages

    return render(request, 'tasks/task2/task2list.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )


def Task2show(request, task1_id):
    listtask = writingtask2.objects.get(pk=task1_id)
    return render(request, 'tasks/task2/task2show.html',
                  {"listtask": listtask}
                  )


class UpdateTask2View(UpdateView):
    model = writingtask2
    form_class = writingtask2Form
    context_object_name = 'post'
    template_name = 'tasks/task2/task2update.html'


class DeleteTask2View(DeleteView):
    model = writingtask2
    template_name = 'tasks/task2/delete_task2.html'
    success_url = reverse_lazy('home')


class AddTask2View(CreateView):
    model = writingtask2
    form_class = writingtask2Form
    template_name = 'tasks/task2/addtask2.html'


""" 
Speaking section
"""

def Speaking(request):
    return render(request, 'speaking/speaking.html',
                  )


def SpeakingPart1Topic(request):
    listtask = speakingpart1.objects.all

    # Set up pagination
    p = Paginator(speakingpart1.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)
    nums = "a" * tasks.paginator.num_pages

    return render(request, 'speaking/part1/part1topiclist.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )
    
    
def SpeakingPart2Questions(request):
    listtask = SpeakingPart2.objects.all

    # Set up pagination
    p = Paginator(SpeakingPart2.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)
    nums = "a" * tasks.paginator.num_pages

    return render(request, 'speaking/part2/part2questionslist.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )
    
    
    
def SpeakingPart3Topic(request):
    listtask = speakingpart3.objects.all

    # Set up pagination
    p = Paginator(speakingpart3.objects.all(), 2)
    page = request.GET.get('page')
    tasks = p.get_page(page)
    nums = "a" * tasks.paginator.num_pages

    return render(request, 'speaking/part3/part3topiclist.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )