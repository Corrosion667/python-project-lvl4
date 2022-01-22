"""Module with views logic of the labels app."""

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView

from task_manager.labels.forms import CreateForm
from task_manager.labels.models import Label
from task_manager.custom_views import CustomListView, CustomLoginMixin, CustomDeleteView


class LabelsListView(CustomListView):
    """View for labels page."""

    template_name = 'labels.html'
    context_object_name = 'labels_list'
    model = Label


class CreateLabelView(SuccessMessageMixin, CustomLoginMixin, CreateView):
    """View for create label page."""

    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')
    template_name = 'create_label.html'
    form_class = CreateForm


class UpdateLabelView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change label name page."""

    model = Label
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully changed')
    template_name = 'update_label.html'
    form_class = CreateForm


class DeleteLabelView(CustomDeleteView):
    """View for label deletion page."""

    model = Label
    template_name = 'delete_label.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    deletion_error_message = _(
        'Can not delete label because it is in use',
    )
