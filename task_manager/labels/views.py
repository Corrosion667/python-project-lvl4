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
