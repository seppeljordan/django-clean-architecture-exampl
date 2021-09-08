from typing import List

from todo.models import Todo
from todo.use_cases import TodosDatabaseGateway


class TodosDatabaseGatewayImpl(TodosDatabaseGateway):
    def add_todo(self) -> None:
        Todo.objects.create()

    def get_all_todos(self) -> List[None]:
        return [None for _ in Todo.objects.all()]
