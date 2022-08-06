
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),

    path('task1categories', task1categories, name='task1categories'),
    path('task1categories/<str:task1type>', task1list, name='task1type'),


]
