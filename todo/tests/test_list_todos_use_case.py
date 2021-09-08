from __future__ import annotations

from unittest import TestCase

from .dependency_injection import DependencyInjector


class ListTodosTestCase(TestCase):
    def setUp(self):
        injector = DependencyInjector()
        self.list_todos = injector.get_list_todos_use_case()
        self.todo_generator = injector.get_todo_generator()

    def test_that_by_default_no_todos_are_listed(self):
        response = self.list_todos()
        self.assertFalse(response.todos)

    def test_that_todos_list_is_not_empty_when_todo_was_added_before(self):
        self.todo_generator.create_todo()
        response = self.list_todos()
        self.assertTrue(response.todos)
