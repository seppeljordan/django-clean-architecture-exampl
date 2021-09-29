from unittest import TestCase

from todo.presenter import TodosListPresenter
from todo.use_cases import ListedTodo, ListTodosResponse


class TodosListPresenterTests(TestCase):
    def setUp(self):
        self.presenter = TodosListPresenter()
        self.empty_response = ListTodosResponse(todos=[])

    def test_that_todo_count_label_shows_0_when_no_todos_are_found(self):
        view_model = self.presenter.present(self.empty_response)
        self.assertEqual(view_model.todo_count_label_text, "0")

    def test_that_todo_count_label_shows_1_when_one_todo_is_found(self):
        view_model = self.presenter.present(
            ListTodosResponse(todos=[ListedTodo(text="test text")])
        )
        self.assertEqual(view_model.todo_count_label_text, "1")

    def test_empty_todo_listing_when_use_case_response_is_empty(self) -> None:
        view_model = self.presenter.present(self.empty_response)
        self.assertFalse(view_model.todo_listing)

    def test_todo_listing_is_not_empty_when_response_contains_one_todo(self) -> None:
        view_model = self.presenter.present(
            ListTodosResponse(
                todos=[ListedTodo("test todo")],
            )
        )
        self.assertTrue(view_model.todo_listing)

    def test_todo(self) -> None:
        expected_todo_text = "test todo"
        view_model = self.presenter.present(
            ListTodosResponse(
                todos=[ListedTodo(expected_todo_text)],
            )
        )
        self.assertEqual(view_model.todo_listing[0], expected_todo_text)
