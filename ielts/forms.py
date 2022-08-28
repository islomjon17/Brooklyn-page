from django import forms
from django.forms import ModelForm
from .models import *


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




#speaking form


class SpeakingPart1Topicform(ModelForm):
    class Meta:
        model = SpeakingPartOneTopic
        fields = "__all__"


class SpeakingPart1form(ModelForm):
    class Meta:
        model = SpeakingPartOne
        fields = "__all__"





class SpeakingPart2form(ModelForm):
    class Meta:
        model = SpeakingPart2
        fields = "__all__"





class SpeakingPart3Topicform(ModelForm):
    class Meta:
        model = SpeakingPartThreeTopic
        fields = "__all__"




class SpeakingPart3form(ModelForm):
    class Meta:
        model = SpeakingPartThree
        fields = "__all__"

