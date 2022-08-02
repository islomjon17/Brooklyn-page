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


class writingtask1(models.Model):
    title = models.CharField(max_length=300)
    text = RichTextField(blank=True, null=True)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')
    score = models.IntegerField(null=True, blank=True)
    type_task = models.CharField(
        max_length=250, choices=TYPES, default="none")
