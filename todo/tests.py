from __future__ import annotations

from functools import lru_cache
from unittest import TestCase
from typing import List
from dataclasses import dataclass
from todo.use_cases import ListTodosUseCase, AddTodoUseCase, AddTodoRequest, TodosDatabaseGateway


singleton = lru_cache(None)


class DependencyInjector:
    def get_list_todos_use_case(self) -> ListTodosUseCase:
        return ListTodosUseCase(
            self.get_todos_database_gateway()
        )

    def get_todo_generator(self) -> TodoGenerator:
        return TodoGenerator(
            add_todo=self.get_add_todo_use_case()
        )

    def get_add_todo_use_case(self) -> AddTodoUseCase:
        return AddTodoUseCase(
            self.get_todos_database_gateway()
        )

    @singleton
    def get_todos_database_gateway(self) -> TodosDatabaseGateway:
        return TodoDatabaseGatewayImpl()


class TodoDatabaseGatewayImpl(TodosDatabaseGateway):
    def __init__(self):
        self.todos: List[None] = []

    def add_todo(self) -> None:
        self.todos.append(None)

    def get_all_todos(self) -> List[None]:
        return self.todos


@dataclass
class TodoGenerator:
    add_todo: AddTodoUseCase
    
    def create_todo(self):
        self.add_todo(AddTodoRequest())


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

