from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import List

from todo.use_cases import AddTodoResponse, ListTodosResponse


@dataclass
class TodosListViewModel:
    todo_count_label_text: str

    def to_dict(self):
        return asdict(self)


class TodosListPresenter:
    def present(self, use_case_response_model: ListTodosResponse) -> TodosListViewModel:
        return TodosListViewModel(
            todo_count_label_text=str(len(use_case_response_model.todos))
        )


@dataclass
class AddTodoViewModel:
    messages: List[str]

    def to_dict(self):
        return asdict(self)


class AddTodoPresenter:
    def present(
        self,
        use_case_response: AddTodoResponse,
    ) -> AddTodoViewModel:
        if use_case_response.is_success:
            messages = ["Todo was successfully created."]
        else:
            messages = ["Todo creation failed."]
        return AddTodoViewModel(
            messages=messages,
        )
