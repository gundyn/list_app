# todo_list/todo_app/test.py
from django.test import TestCase
from .models import ToDoList, ToDoItem

class ToDoListTestCase(TestCase):
    def test_todo_list_creation(self):
        list_title = "Test List"
        todo_list = ToDoList.objects.create(title=list_title)
        self.assertEqual(todo_list.title, list_title)
        
class TodoItemTestCase(TestCase):
    def test_todo_item_creation(self):
        list_title = "Test List"
        todo_list = ToDoList.objects.create(title=list_title)

        item_title = "Test Item"
        todo_item = ToDoItem.objects.create(title=item_title, todo_list=todo_list)
        self.assertEqual(todo_item.title, item_title)
        self.assertEqual(todo_item.todo_list, todo_list)

