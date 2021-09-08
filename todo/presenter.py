from __future__ import annotations

from dataclasses import dataclass

from todo.use_cases import ListTodosResponse


@dataclass
class TodosListPresentation:
    todo_count_label_text: str


class TodosListPresenter:
    def present_response(
        self, use_case_response_model: ListTodosResponse
    ) -> TodosListPresentation:
        return TodosListPresentation(
            todo_count_label_text=str(len(use_case_response_model.todos))
        )
