"""Module with views logic of the tasks app."""

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.tasks.forms import CreateForm
from task_manager.tasks.models import Task
from task_manager.users.views import CustomLoginMixin


class TasksListView(CustomLoginMixin, ListView):
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


class CreateTaskView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create task page."""

    model = Task
    success_url = reverse_lazy('tasks')
    template_name = 'create_task.html'
    success_message = _('Task successfully created')
    form_class = CreateForm
    login_url = 'login'

    def form_valid(self, form):
        """Set author of task as active user."""  # noqa: DAR201
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change task data page."""

    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully changed')
    template_name = 'update_task.html'
    form_class = CreateForm
    login_url = 'login'


class DeleteTaskView(SuccessMessageMixin, CustomLoginMixin, DeleteView):
    """View for task deletion page."""

    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')
    login_url = 'login'
