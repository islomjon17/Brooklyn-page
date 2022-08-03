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
    ("barchart", "Bar Chart"), ("linegraph", "Line Graph"), ("table", "Table"),
    ("piechart", " Pie Chart"), ("processdiagram",
                                 "Process Diagram"), ("map", "Map"), ("multiplegraphs", "Multiple Graphs")
)


class writingtask1(models.Model):
    title = models.CharField(max_length=300)
    text = RichTextField(blank=True, null=True)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')
    score = models.IntegerField(null=True, blank=True)
    type_task = models.CharField(
        max_length=250, choices=TYPES, default="none")


class Task2question(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'Category', related_name='category', default="coding", on_delete=models.CASCADE)

    def __str__(self):
        return (self.title)

    def get_absolute_url(self):
        return reverse('home')


class writingtask2(models.Model):
    question = models.ForeignKey(
        'Task2question',  default="coding", on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    text = RichTextField(blank=True, null=True)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return (self.title)
