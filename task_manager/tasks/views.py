"""Module with views logic of the tasks app."""

from django.http import HttpResponse


def main(request):
    """View for tasks main page."""  # noqa: DAR201
    return HttpResponse('No tasks yet')
