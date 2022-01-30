"""Module with views logic of the statuses app."""

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, ListView

from task_manager.custom_views import (
    CustomDeleteView,
    CustomLoginMixin,
)
from task_manager.statuses.models import Status


class StatusesListView(CustomLoginMixin, ListView):
    """View for statuses page."""

    template_name = 'statuses.html'
    context_object_name = 'statuses_list'
    model = Status


class CreateStatusView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create status page."""

    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')
    template_name = 'create_status.html'
    fields = ['name']


class UpdateStatusView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change status name page."""

    model = Status
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully changed')
    template_name = 'update_status.html'
    fields = ['name']


class DeleteStatusView(CustomDeleteView):
    """View for status deletion page."""

    model = Status
    template_name = 'delete_status.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')
    deletion_error_message = _(
        'Can not delete status because it is in use',
    )
