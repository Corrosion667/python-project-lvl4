"""URL routing of the tasks app."""

from django.urls import path

from task_manager.tasks.views import TasksListView, CreateTaskView

urlpatterns = [
    path('', TasksListView.as_view(), name='tasks'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
]
