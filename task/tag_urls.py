from django.urls import path

from task.views import TaskListView, TaskCreateView


app_name = "task"
urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="tag-create"),
]
