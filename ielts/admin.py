from django.contrib import admin
from .models import writingtask2, writingtask1, Task2question, CategoryTask2, CategoryTask1, speakingpart1, SpeakingPartOneTopic


admin.site.register(CategoryTask2)
admin.site.register(writingtask1)
admin.site.register(writingtask2)
admin.site.register(Task2question)
admin.site.register(CategoryTask1)
admin.site.register(speakingpart1)
admin.site.register(SpeakingPartOneTopic)
