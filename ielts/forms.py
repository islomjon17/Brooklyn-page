from django import forms
from django.forms import ModelForm
from .models import CategoryTask2, CategoryTask1, WritingTaskOne, Task2question, WritingTaskTwo


class CategoryForm(ModelForm):
    class Meta:
        model = CategoryTask2
        fields = "__all__"


class CategoryTask1Form(ModelForm):
    class Meta:
        model = CategoryTask1
        fields = "__all__"


class writingtask1Form(ModelForm):
    class Meta:
        model = WritingTaskOne
        fields = "__all__"


class Task2questionForm(ModelForm):
    class Meta:
        model = Task2question
        fields = "__all__"


class writingtask2Form(ModelForm):
    class Meta:
        model = WritingTaskTwo
        fields = "__all__"
