
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('task1show/<int:pk>/', task1show, name='task1show'),
    path('task1list', task1list, name='task1')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
