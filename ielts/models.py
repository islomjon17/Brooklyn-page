from turtle import title
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.


class CategoryTask2(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('home')


class CategoryTask1(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('home')


class writingtask1(models.Model):
    title = models.CharField(max_length=300)
    text = RichTextField(blank=True, null=True)
    cover = models.ImageField(null=True, blank=True, upload_to='images/')
    score = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(
        'CategoryTask1', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.category} {self.title}'

    def get_absolute_url(self):
        return reverse('home')


class Task2question(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        'CategoryTask2', related_name='category', default="without any category", on_delete=models.CASCADE)

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

    def get_absolute_url(self):
        return reverse('home')


class speakingtopic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('home')
    
    
TOPIC_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
)
class SpeakingPartOneTopic(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return (self.title)

    def get_absolute_url(self):
        return reverse('home')


class speakingpart1(models.Model):
    topic = models.ForeignKey(
        'SpeakingPartOneTopic',  default="unnamed", on_delete=models.CASCADE)
    
    question1 = models.CharField(max_length=255)
    answer1 = models.TextField()
    
    question2 = models.CharField(max_length=255, blank=True)
    answer2 = models.TextField(blank=True)
    
    question3 = models.CharField(max_length=255, blank=True)
    answer3 = models.TextField(blank=True)
    
    question4 = models.CharField(max_length=255, blank=True)
    answer4 = models.TextField(blank=True)
    
    question5 = models.CharField(max_length=255, blank=True)
    answer5 = models.TextField(blank=True)
    
    question6 = models.CharField(max_length=255, blank=True)
    answer6 = models.TextField(blank=True)
    
    question7 = models.CharField(max_length=255, blank=True)
    answer7 = models.TextField(blank=True)
    
    question8 = models.CharField(max_length=255, blank=True)
    answer8 = models.TextField(blank=True)
    
    
    
class SpeakingPart2(models.Model):
    question = models.CharField(max_length=255)
    text = RichTextField(blank=True, null=True)

    
    

    
