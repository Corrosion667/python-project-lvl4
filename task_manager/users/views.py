from django.views.generic import TemplateView


class UsersListView(TemplateView):
    """View for users page."""

    template_name = 'users.html'
