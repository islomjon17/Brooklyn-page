from turtle import title
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('home')


TYPES = (
    ("Bar Chart", "Bar Chart"), ("Line Graph", "Line Graph"), ("Table", "Table"),
    (" Pie Chart", " Pie Chart"), ("Process Diagram",
                                   "Process Diagram"), ("Map", "Map"), ("Multiple Graphs", "Multiple Graphs")
)
