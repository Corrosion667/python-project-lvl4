from django.shortcuts import render
from django.views.generic import TemplateView

class MainPageView(TemplateView):
    """View for root site page."""
    template_name = 'main.html'


def users(request):
    """View for users page."""
    return render(request, 'users.html')
