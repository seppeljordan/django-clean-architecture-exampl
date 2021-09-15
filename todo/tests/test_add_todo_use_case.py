from unittest import TestCase

from todo.use_cases import AddTodoRequest

from .dependency_injection import DependencyInjector


class AddTodoUseCaseTests(TestCase):
    def setUp(self):
        injector = DependencyInjector()
        self.list_todos = injector.get_list_todos_use_case()
        self.add_todo = injector.get_add_todo_use_case()

    def test_when_adding_a_todo_its_text_shows_up_in_the_todo_listing(self):
        self.add_todo(
            AddTodoRequest(
                text="test todo",
            )
        )
        self.assertTextInTodos("test todo")

    def assertTextInTodos(self, text: str) -> None:
        response = self.list_todos()
        self.assertIn(text, [todo.text for todo in response.todos])
