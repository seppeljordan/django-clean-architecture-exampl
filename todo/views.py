from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from todo.controllers import AddTodoController
from todo.database_gateway import TodosDatabaseGatewayImpl
from todo.presenter import AddTodoPresenter, TodosListPresenter
from todo.use_cases import AddTodoUseCase, ListTodosUseCase

from .forms import AddTodoForm


class DependencyInjector:
    def get_add_todos_use_case(self) -> AddTodoUseCase:
        return AddTodoUseCase(self.get_todos_database_gateway())

    def get_todos_database_gateway(self) -> TodosDatabaseGatewayImpl:
        return TodosDatabaseGatewayImpl()

    def get_todos_list_todos_use_case(self) -> ListTodosUseCase:
        return ListTodosUseCase(self.get_todos_database_gateway())

    def get_todos_list_presenter(self) -> TodosListPresenter:
        return TodosListPresenter()

    def get_add_todo_presenter(self) -> AddTodoPresenter:
        return AddTodoPresenter()

    def get_add_todo_controller(self) -> AddTodoController:
        return AddTodoController()


def todo_list_view(request):
    injector = DependencyInjector()
    list_todos = injector.get_todos_list_todos_use_case()
    presenter = injector.get_todos_list_presenter()
    presentation = presenter.present(
        list_todos(),
    )
    return render(
        request,
        "todo/todo-list.html",
        context=presentation.to_dict(),
    )


class AddTodoView(FormView):
    form_class = AddTodoForm
    template_name = "todo/add-todo.html"
    success_url = reverse_lazy("todo-list")

    def form_valid(self, form):
        injector = DependencyInjector()
        controller = injector.get_add_todo_controller()
        presenter = injector.get_add_todo_presenter()
        add_todos = injector.get_add_todos_use_case()
        use_case_request = controller.process_user_input(form)
        use_case_response = add_todos(use_case_request)
        view_model = presenter.present(use_case_response)
        for message in view_model.messages:
            messages.add_message(self.request, messages.INFO, message)
        return super().form_valid(form)
