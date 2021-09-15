from dataclasses import dataclass
from unittest import TestCase

from todo.controllers import AddTodoController, AddTodoForm, InvalidFormData


@dataclass
class AddTodoTestForm(AddTodoForm):
    todo_text: str

    def get_todo_text(self) -> str:
        return self.todo_text


class AddTodoControllerTests(TestCase):
    def setUp(self):
        self.controller = AddTodoController()

    def test_that_input_longer_than_1000_chars_raises_exception(self):
        with self.assertRaises(InvalidFormData):
            self.controller.process_user_input(
                AddTodoTestForm(
                    todo_text="1" * 1001,
                )
            )

    def test_that_input_with_length_0_raises_exception(self):
        with self.assertRaises(InvalidFormData):
            self.controller.process_user_input(
                AddTodoTestForm(
                    todo_text="",
                )
            )

    def test_that_input_with_length_1000_does_not_raiseException(self):
        self.controller.process_user_input(
            AddTodoTestForm(
                todo_text="1" * 1000,
            )
        )

    def test_that_valid_form_data_goes_into_use_case_request(self):
        request_model = self.controller.process_user_input(
            AddTodoTestForm(
                todo_text="test string",
            )
        )
        self.assertEqual(
            request_model.text,
            "test string",
        )
