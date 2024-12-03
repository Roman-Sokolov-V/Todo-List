from django.urls import path

from task.views import TaskListView, TaskCreateView


app_name = "task"
urlpatterns = [
    path("home/", TaskListView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
]
