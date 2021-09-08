from uuid import uuid4

from django.db import models


class Todo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
