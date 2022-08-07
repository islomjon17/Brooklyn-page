from django import forms
from django.forms import ModelForm
from .models import Category, CategoryTask1, writingtask1, Task2question, writingtask2


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryTask1Form(ModelForm):
    class Meta:
        model = CategoryTask1
        fields = "__all__"


class writingtask1Form(ModelForm):
    class Meta:
        model = writingtask1
        fields = "__all__"


class Task2questionForm(ModelForm):
    class Meta:
        model = Task2question
        fields = "__all__"


class writingtask2Form(ModelForm):
    class Meta:
        model = writingtask2
        fields = "__all__"