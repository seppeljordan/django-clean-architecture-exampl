from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import List

from todo.use_cases import (
    AddTodoRequest,
    AddTodoUseCase,
    ListTodosUseCase,
    TodosDatabaseGateway,
)

singleton = lru_cache(None)


class DependencyInjector:
    def get_list_todos_use_case(self) -> ListTodosUseCase:
        return ListTodosUseCase(self.get_todos_database_gateway())

    def get_todo_generator(self) -> TodoGenerator:
        return TodoGenerator(add_todo=self.get_add_todo_use_case())

    def get_add_todo_use_case(self) -> AddTodoUseCase:
        return AddTodoUseCase(self.get_todos_database_gateway())

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
