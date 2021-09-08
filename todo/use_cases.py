from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class TodosDatabaseGateway(ABC):
    @abstractmethod
    def add_todo(self) -> None:
        pass

    @abstractmethod
    def get_all_todos(self) -> List[None]:
        pass


class AddTodoRequest:
    pass


@dataclass
class AddTodoUseCase:
    todos_db_gateway: TodosDatabaseGateway

    def __call__(self, request: AddTodoRequest):
        self.todos_db_gateway.add_todo()


@dataclass
class ListTodosResponse:
    todos: List[None]


@dataclass
class ListTodosUseCase:
    todos_db_gateway: TodosDatabaseGateway

    def __call__(self):
        return ListTodosResponse(todos=self.todos_db_gateway.get_all_todos())


class CompleteTodoUseCase:
    pass


class EditTodoUseCase:
    pass


class DeleteTodoUseCase:
    pass
