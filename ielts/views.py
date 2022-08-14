from re import L
from django.shortcuts import render, redirect
from .models import writingtask1, CategoryTask1
from django.views.generic import ListView
from .forms import writingtask1Form
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

    return render(request, 'task1list.html',
                  {"listtask": listtask,
                   "tasks": tasks,
                   "nums": nums,
                   }
                  )


def Task1show(request, task1_id):
    listtask = writingtask1.objects.get(pk=task1_id)
    return render(request, 'task1show.html',
                  {"listtask": listtask}
                  )


class UpdateTask1View(UpdateView):
    model = writingtask1
    form_class = writingtask1Form
    context_object_name = 'post'
    template_name = 'task1update.html'


class DeleteTask1View(DeleteView):
    model = writingtask1
    template_name = 'delete_task1.html'
    success_url = reverse_lazy('home')


class AddTaskView(CreateView):
    model = writingtask1
    form_class = writingtask1Form
    template_name = 'addtask1.html'
