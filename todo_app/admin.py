# todo_list/todo_app/admin.py
from django.contrib import admin
from .models import ToDoList, ToDoItem

admin.site.register(ToDoList)
admin.site.register(ToDoItem)
