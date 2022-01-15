from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView

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
        """Return users list."""
        return User.objects.all()


class SignupView(CreateView):
    """View for signup page."""

    model = User
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    form_class = SignupForm


class UpdateUserView(UpdateView):
    model = User
    template_name = 'update_user.html'
    success_url = reverse_lazy('users')
    form_class = SignupForm


class UserLoginView(LoginView):
    """View for users page."""

    template_name = 'login.html'
    next_page = reverse_lazy('main')


class UserLogoutView(LogoutView):

    next_page = reverse_lazy('main')
