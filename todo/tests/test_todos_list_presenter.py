from unittest import TestCase

from todo.presenter import TodosListPresenter
from todo.use_cases import ListedTodo, ListTodosResponse


class TodosListPresenterTests(TestCase):
    def setUp(self):
        self.presenter = TodosListPresenter()

    def test_that_todo_count_label_shows_0_when_no_todos_are_found(self):
        presentation = self.presenter.present(ListTodosResponse(todos=[]))
        self.assertEqual(presentation.todo_count_label_text, "0")

    def test_that_todo_count_label_shows_1_when_one_todo_is_found(self):
        presentation = self.presenter.present(
            ListTodosResponse(todos=[ListedTodo(text="test text")])
        )
        self.assertEqual(presentation.todo_count_label_text, "1")
