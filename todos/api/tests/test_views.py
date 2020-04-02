import json

from django.test import TestCase

from ..models import TodoItem

class TodoItemViewsetTests(TestCase):
    def setUp(self):
        TodoItem.objects.create(title='Create Tests')

    def test_todos_get(self):
        response = self.client.get('/api/todoItems/')
        self.assertEqual(response.status_code, 200)

        items = json.loads(response.content)
        self.assertEqual(len(items), 1)

        item = items[0]
        self.assertEqual(item['title'], 'Create Tests')