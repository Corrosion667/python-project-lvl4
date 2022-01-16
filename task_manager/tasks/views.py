"""Module with views logic of the tasks app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from task_manager.tasks.forms import CreateForm
from task_manager.tasks.models import Task


class TasksListView(LoginRequiredMixin, ListView):
    """View for tasks page."""

    template_name = 'tasks.html'
    context_object_name = 'tasks_list'
    login_url = 'login'

    def get_queryset(self):
        """Get list of tasks.

        Returns:
            The list of all tasks.
        """
        return Task.objects.all()


class CreateTaskView(LoginRequiredMixin, CreateView):
    """View for create task page."""

    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'create_task.html'
    form_class = CreateForm
    login_url = 'login'
