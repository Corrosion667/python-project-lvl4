from django.views.generic import TemplateView, CreateView
from task_manager.users.forms import SignupForm
from django.urls import reverse_lazy
from task_manager.users.models import User
from django.urls import reverse_lazy


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'


class SignupView(CreateView):
    """View for signup page."""
    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignupForm


class LoginView(TemplateView):
    """View for users page."""

    template_name = 'login.html'


class UsersListView(TemplateView):
    """View for users page."""

    template_name = 'users.html'
