from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


class TodoDatabaseModel(ABC):
    @abstractmethod
    def get_text(self):
        pass


class TodosDatabaseGateway(ABC):
    @abstractmethod
    def add_todo(self, text: str) -> None:
        pass

    @abstractmethod
    def get_all_todos(self) -> List[TodoDatabaseModel]:
        pass


@dataclass
class AddTodoRequest:
    text: str


@dataclass
class AddTodoUseCase:
    todos_db_gateway: TodosDatabaseGateway

    def __call__(self, request: AddTodoRequest):
        self.todos_db_gateway.add_todo(text=request.text)


@dataclass
class ListedTodo:
    text: str


@dataclass
class ListTodosResponse:
    todos: List[ListedTodo]


@dataclass
class ListTodosUseCase:
    todos_db_gateway: TodosDatabaseGateway

    def __call__(self):
        db_todos = self.todos_db_gateway.get_all_todos()
        return ListTodosResponse(
            todos=[ListedTodo(text=db_todo.get_text()) for db_todo in db_todos]
        )


class CompleteTodoUseCase:
    pass


class EditTodoUseCase:
    pass


class DeleteTodoUseCase:
    pass
