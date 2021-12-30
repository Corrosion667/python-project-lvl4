from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    """View for tasks main page."""
    return HttpResponse('No tasks yet')
