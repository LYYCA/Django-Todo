from django.test import TestCase

from .models import Todo
# Create your tests here.

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='todo 1', body='test body')
    
    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEquals(expected_object_name, 'todo 1')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = f'{todo.body}'
        self.assertEquals(expected_object_body, 'test body')