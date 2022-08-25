
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', Home, name='home'),
    path('task1show/<int:task1_id>/', Task1show, name='task1show'),
    path('task1list', Task1list, name='task1list'),
    path('task1update/<int:pk>/',
         UpdateTask1View.as_view(), name='task1update'),
    path('tasl1delete/<int:pk>/',
         DeleteTask1View.as_view(), name='tasl1delete'),
    path('addtask1',
         AddTaskView.as_view(), name='addtask1'),
    # task 2 section
    path('task2list', Task2list, name='task2list'),
    path('task2show/<int:task1_id>/', Task2show, name='task2show'),
    path('task2update/<int:pk>/',
         UpdateTask2View.as_view(), name='task2update'),
    path('task2delete/<int:pk>/',
         DeleteTask2View.as_view(), name='task2delete'),
    path('addtask2',
         AddTask2View.as_view(), name='addtask2'),

##############speaking urls

     path('speaking/', Speaking, name='speaking' )

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
