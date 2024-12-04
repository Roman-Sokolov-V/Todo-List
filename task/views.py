from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect

from task.models import Task, Tag
from task.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/create_update_form.html"
    success_url = reverse_lazy("home")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task/tag_confirm_delete.html"
    success_url = reverse_lazy("tags")


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done  # Перемикання статусу
    task.save()
    return redirect(reverse("home"))
