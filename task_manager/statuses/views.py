from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.statuses.models import Status
from task_manager.statuses.forms import CreateForm
from django.urls import reverse_lazy


class StatusesListView(LoginRequiredMixin, ListView):
    template_name = 'statuses.html'
    context_object_name = 'statuses_list'
    login_url = 'login'

    def get_queryset(self):
        """Return statuses list."""
        return Status.objects.all()


class CreateStatusView(LoginRequiredMixin, CreateView):
    """View for create status page."""
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'create_status.html'
    form_class = CreateForm
    login_url = 'login'


class UpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Status
    success_url = reverse_lazy('statuses')
    template_name = 'update_status.html'
    form_class = CreateForm
    login_url = 'login'


class DeleteStatusView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete_status.html'
    success_url = reverse_lazy('statuses')
    login_url = 'login'
