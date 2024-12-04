"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from task.views import (
    TaskListView, TaskCreateView, TagListView, TagCreateView, TagUpdateView,
    TagDeleteView, toggle_task_status, remove_tag, TaskUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", TaskListView.as_view(), name="home"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/<int:pk>/toggle/", toggle_task_status, name="task-toggle"),
    path("task/<int:pk>/<int:tag_pk>", remove_tag,
         name="remove-tag"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update-tag"),
]
