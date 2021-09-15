from typing import List

from todo.models import Todo
from todo.use_cases import TodoDatabaseModel, TodosDatabaseGateway


class TodosDatabaseGatewayImpl(TodosDatabaseGateway):
    def add_todo(self, text: str) -> None:
        Todo.objects.create()

    def get_all_todos(self) -> List[TodoDatabaseModel]:
        return list(Todo.objects.all())
