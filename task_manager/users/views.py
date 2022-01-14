from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """View for root site page."""

    template_name = 'main_page.html'


class LoginView(TemplateView):
    """View for users page."""

    template_name = 'login.html'


class UsersListView(TemplateView):
    """View for users page."""

    template_name = 'users.html'
