from django.views import generic
from django.shortcuts import render

from schedule.models import Task, Tag

class TaskListView(generic.ListView):
    model = Task
    template_name = "templates/schedule/task_list.html"
