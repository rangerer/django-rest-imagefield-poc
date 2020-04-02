from datetime import date

from django.test import TestCase

from ..models import TodoItem

# Create your tests here.

class TodoItemModelTests(TestCase):
    def setUp(self):
        TodoItem.objects.create(title='Create Tests')
        TodoItem.objects.create(title='Fix Bugs', due=date.today())
    
    def test_all_todos(self):
        items = TodoItem.objects.all()
        self.assertEqual(items.count(), 2)
    
    def test_todays_todos(self):
        items = TodoItem.objects.filter(due=date.today())
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, 'Fix Bugs')