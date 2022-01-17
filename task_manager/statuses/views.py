"""Module with views logic of the statuses app."""

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.statuses.forms import CreateForm
from task_manager.statuses.models import Status
from task_manager.users.views import CustomLoginMixin


class StatusesListView(CustomLoginMixin, ListView):
    """View for statuses page."""

    template_name = 'statuses.html'
    context_object_name = 'statuses_list'
    login_url = 'login'

    def get_queryset(self):
        """Get list of statuses.

        Returns:
            The list of all statuses.
        """
        return Status.objects.all()


class CreateStatusView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create status page."""

    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')
    template_name = 'create_status.html'
    form_class = CreateForm
    login_url = 'login'


class UpdateStatusView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change status name page."""

    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')
    template_name = 'update_status.html'
    form_class = CreateForm
    login_url = 'login'


class DeleteStatusView(SuccessMessageMixin, CustomLoginMixin, DeleteView):
    """View for status deletion page."""

    model = Status
    template_name = 'delete_status.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    login_url = 'login'
