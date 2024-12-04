from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "content",
            "deadline",
            "tag",
        ]  # Вкажіть поля, які повинні відображатися у формі
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter task description",
                }
            ),
            "deadline": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "tag": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
