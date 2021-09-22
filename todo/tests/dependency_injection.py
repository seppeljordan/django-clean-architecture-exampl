from __future__ import annotations

import random
import string
from dataclasses import dataclass
from functools import lru_cache
from typing import List

from todo.use_cases import (
    AddTodoRequest,
    AddTodoUseCase,
    ListTodosUseCase,
    TodoDatabaseModel,
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
        return TodoDatabaseGatewayTestImpl()


class TodoDatabaseModelImpl(TodoDatabaseModel):
    def __init__(self, text: str) -> None:
        self.text = text

    def get_text(self) -> str:
        return self.text


class TodoDatabaseGatewayTestImpl(TodosDatabaseGateway):
    def __init__(self):
        self.todos: List[TodoDatabaseModelImpl] = []

    def add_todo(self, text: str) -> None:
        self.todos.append(TodoDatabaseModelImpl(text=text))

    def get_all_todos(self) -> List[TodoDatabaseModel]:
        return list(self.todos)

    def has_todo_with_text(self, text: str) -> bool:
        return any(todo.get_text() == text for todo in self.todos)


@dataclass
class TodoGenerator:
    add_todo: AddTodoUseCase

    def create_todo(self):
        self.add_todo(AddTodoRequest(text=self._get_random_string()))

    def _get_random_string(self):
        max_size = 1000
        size = random.randint(0, max_size)
        allowed_characters = string.ascii_letters + string.punctuation
        return "".join(random.choice(allowed_characters) for x in range(size))
