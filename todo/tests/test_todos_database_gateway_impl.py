from django.test import TestCase

from todo.database_gateway import TodosDatabaseGatewayImpl


class TodosDatabaseGatewayImplTestCase(TestCase):
    def setUp(self):
        self.db_gateway = TodosDatabaseGatewayImpl()

    def test_that_by_default_no_todos_are_returned(self):
        self.assertFalse(self.db_gateway.get_all_todos())

    def test_that_todos_returned_are_not_empty_when_one_was_added_before(self):
        self.db_gateway.add_todo()
        self.assertTrue(self.db_gateway.get_all_todos())
