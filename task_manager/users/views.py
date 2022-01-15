"""Module with views logic of the users app."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from task_manager.users.forms import SignupForm
from task_manager.users.models import User


class MainPageView(TemplateView):
    """View for main (home) site page."""

    template_name = 'main_page.html'


class UsersListView(ListView):
    """View for users page."""

    template_name = 'users.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        """Get list of users.

        Returns:
            The list of all users.
        """
        return User.objects.all()


class SignupView(CreateView):
    """View for signup page."""

    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignupForm


class UpdateUserView(LoginRequiredMixin, UpdateView):
    """View for change user data page."""

    model = User
    template_name = 'update_user.html'
    success_url = reverse_lazy('users')
    form_class = SignupForm
    login_url = 'login'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    """View for user deletion page."""

    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('users')
    login_url = 'login'


class UserLoginView(LoginView):
    """View for login page."""

    template_name = 'login.html'
    next_page = reverse_lazy('main')


class UserLogoutView(LogoutView):
    """View for logout page."""

    next_page = reverse_lazy('main')
