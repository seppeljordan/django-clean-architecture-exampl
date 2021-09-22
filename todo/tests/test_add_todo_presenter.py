from unittest import TestCase

from todo.presenter import AddTodoPresenter
from todo.use_cases import AddTodoResponse


class AddTodoPresenterTests(TestCase):
    def setUp(self):
        self.presenter = AddTodoPresenter()

    def test_when_todo_was_created_successfully_then_show_success_message(self):
        use_case_response = AddTodoResponse(is_success=True)
        presentation = self.presenter.present(use_case_response)
        self.assertIn(
            "Todo was successfully created.",
            presentation.messages,
        )

    def test_when_todo_creation_failed_then_show_failure_message(self):
        use_case_response = AddTodoResponse(is_success=False)
        presentation = self.presenter.present(use_case_response)
        self.assertIn(
            "Todo creation failed.",
            presentation.messages,
        )
