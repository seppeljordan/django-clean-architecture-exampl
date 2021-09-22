from django.test import TestCase

from todo.database_gateway import TodosDatabaseGatewayImpl


class TodosDatabaseGatewayImplTestCase(TestCase):
    def setUp(self):
        self.db_gateway = TodosDatabaseGatewayImpl()

    def test_that_by_default_no_todos_are_returned(self):
        self.assertFalse(self.db_gateway.get_all_todos())

    def test_with_empty_database_no_todo_with_random_text_is_in_database(self):
        self.assertFalse(self.db_gateway.has_todo_with_text("test text"))

    def test_that_todos_are_found_with_exact_text_queried(self):
        self.db_gateway.add_todo("test text")
        self.assertTrue(self.db_gateway.has_todo_with_text("test text"))

    def test_that_todos_are_not_found_by_text_if_it_isnt_a_exact_match(self):
        self.db_gateway.add_todo("test text")
        self.assertFalse(self.db_gateway.has_todo_with_text("other text"))

    def test_that_todos_returned_are_not_empty_when_one_was_added_before(self):
        self.db_gateway.add_todo(text="test text")
        self.assertTrue(self.db_gateway.get_all_todos())
