from django.views.generic import TemplateView


class MainPageView(TemplateView):
    """View for root site page."""

    template_name = 'main_page.html'
