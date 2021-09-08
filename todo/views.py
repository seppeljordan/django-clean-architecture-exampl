from django.shortcuts import render

from todo.database_gateway import TodosDatabaseGatewayImpl
from todo.presenter import TodosListPresenter
from todo.use_cases import ListTodosUseCase


def todo_list_view(request):
    list_todos = ListTodosUseCase(TodosDatabaseGatewayImpl())
    presentation = TodosListPresenter().present_response(
        list_todos(),
    )
    return render(
        request,
        "todo/todo-list.html",
        context=presentation.to_dict(),
    )
