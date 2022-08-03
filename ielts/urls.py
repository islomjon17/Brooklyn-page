
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),

    path('task1categories', task1categories, name='task1categories')



]
