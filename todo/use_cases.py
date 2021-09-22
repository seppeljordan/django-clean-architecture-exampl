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

    @abstractmethod
    def has_todo_with_text(self, text: str) -> bool:
        pass


@dataclass
class AddTodoRequest:
    text: str


@dataclass
class AddTodoResponse:
    is_success: bool


@dataclass
class AddTodoUseCase:
    todos_db_gateway: TodosDatabaseGateway

    def __call__(self, request: AddTodoRequest) -> AddTodoResponse:
        if self.todos_db_gateway.has_todo_with_text(request.text):
            return AddTodoResponse(is_success=False)
        self.todos_db_gateway.add_todo(text=request.text)
        return AddTodoResponse(is_success=True)


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
