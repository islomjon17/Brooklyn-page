from django.contrib import admin
from .models import writingtask2, writingtask1, Task2question, Category, CategoryTask1
# Register your models here.


admin.site.register(Category)
admin.site.register(writingtask1)
admin.site.register(writingtask2)
admin.site.register(Task2question)
admin.site.register(CategoryTask1)
