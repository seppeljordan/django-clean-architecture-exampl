from abc import ABC, abstractmethod

from .use_cases import AddTodoRequest


class InvalidFormData(Exception):
    pass


class AddTodoForm(ABC):
    @abstractmethod
    def get_todo_text(self) -> str:
        pass


class AddTodoController:
    def process_user_input(self, form: AddTodoForm) -> AddTodoRequest:
        text = form.get_todo_text()
        if len(text) > 0 and len(text) <= 1000:
            return AddTodoRequest(
                text=text,
            )
        raise InvalidFormData()
