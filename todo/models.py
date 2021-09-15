from uuid import uuid4

from django.db import models

from todo.use_cases import TodoDatabaseModel


class Todo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.TextField()

    def get_text(self) -> str:
        return self.text


TodoDatabaseModel.register(Todo)
