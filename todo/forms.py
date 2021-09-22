from django import forms

from . import controllers


class AddTodoForm(forms.Form):
    text = forms.CharField()

    def get_todo_text(self) -> str:
        return self.cleaned_data["text"]


controllers.AddTodoForm.register(AddTodoForm)
