
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

     path('speaking/', Speaking, name='speaking' ),
     path('speakingpart1/', SpeakingPart1Topic, name='speakingpart1'),
     path('speakingpart2/', SpeakingPart2Questions, name='speakingpart2'),
     path('speakingpart3/', SpeakingPart3Topic, name='speakingpart3'),
     path('speakingpart1show/<int:id>/', part1sample, name='speakingpart1show'),
     path('speakingpart2show/<int:id>/', part2sample, name='speakingpart2show'),
     path('speakingpart3show/<int:id>/', part3sample, name='speakingpart3show'),
     #update and edit section
     path('speakingpartupdate/<int:pk>/',
         UpdateSpeakingPart1View.as_view(), name='speakingpartupdate'),
     path('speakingpart2update/<int:pk>/',
         UpdateSpeakingPart2View.as_view(), name='speakingpart2update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
