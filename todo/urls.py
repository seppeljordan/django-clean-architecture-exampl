from django.urls import path

from todo.views import AddTodoView, todo_list_view

urlpatterns = [
    path("todos/add/", AddTodoView.as_view(), name="add-todo"),
    path("todos/", todo_list_view, name="todo-list"),
]
