"""Module with views logic of the statuses app."""

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import CreateForm
from task_manager.labels.models import Label
from task_manager.users.views import CustomLoginMixin

from django.http import HttpResponse


def main(request):
    """View for labels main page."""
    return HttpResponse('No labels yet')


class CreateLabelView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create label page."""

    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    template_name = 'create_label.html'
    form_class = CreateForm
    login_url = 'login'


class UpdateLabelView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change label name page."""

    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully changed')
    template_name = 'update_label.html'
    form_class = CreateForm
    login_url = 'login'


class DeleteLabelView(SuccessMessageMixin, CustomLoginMixin, DeleteView):
    """View for status deletion page."""

    model = Label
    template_name = 'delete_label.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    login_url = 'login'
    deletion_error_message = _(
        'Can not delete label because it is in use',
    )

    def post(self, request, *args, **kwargs):
        """POST requests method.

        Returns:
            Execute POST request or redirect if user tries to delete label in use.
        """
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                self.request, self.deletion_error_message,
            )
            return redirect('labels')
