"""Module with views logic of the users app."""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
)

from task_manager.users.forms import SignupForm
from task_manager.users.models import User


class CustomLoginMixin(LoginRequiredMixin):
    """Mixin with added login required message."""

    denied_without_login_message = _('You are not authorized! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        """Redirect unauthenticated users using error message.

        Returns:
            Redirect if user is not authenticated.
        """
        if not request.user.is_authenticated:
            messages.error(self.request, self.denied_without_login_message)
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


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


class SignupView(SuccessMessageMixin, CreateView):
    """View for signup page."""

    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignupForm
    success_message = _('User successfully registered')


class UpdateUserView(SuccessMessageMixin, CustomLoginMixin, UpdateView):
    """View for change user data page."""

    model = User
    template_name = 'update_user.html'
    success_url = reverse_lazy('users')
    form_class = SignupForm
    login_url = 'login'
    success_message = _('User successfully changed')
    unable_to_change_others_message = _(
        'You do not have permission to change another user.',
    )

    def get(self, request, *args, **kwargs):
        """GET requests method.

        Returns:
            Execute GET request or redirect if user tries to change other users.
        """
        if request.user != User.objects.get(pk=self.kwargs['pk']):
            messages.error(
                self.request, self.unable_to_change_others_message,
            )
            return redirect('users')
        return super().get(request, *args, **kwargs)


class DeleteUserView(SuccessMessageMixin, CustomLoginMixin, DeleteView):
    """View for user deletion page."""

    model = User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('users')
    login_url = 'login'
    success_message = _('User successfully deleted')
    unable_to_change_others_message = _(
        'You do not have permission to change another user.',
    )
    deletion_error_message = _(
        'Cannot delete user because it is in use',
    )

    def get(self, request, *args, **kwargs):
        """GET requests method.

        Returns:
            Execute GET request or redirect if user tries to change other users.
        """
        if request.user != User.objects.get(pk=self.kwargs['pk']):
            messages.error(
                self.request, self.unable_to_change_others_message,
            )
            return redirect('users')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST requests method.

        Returns:
            Execute POST request or redirect if user tries to delete user in use.
        """
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                self.request, self.deletion_error_message,
            )
            return redirect('users')


class UserLoginView(SuccessMessageMixin, LoginView):
    """View for login page."""

    template_name = 'login.html'
    next_page = reverse_lazy('main')
    success_message = _('You are logged in')


class UserLogoutView(LogoutView):
    """View for logout page."""

    next_page = reverse_lazy('main')
