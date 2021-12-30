from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    """View for statuses main page."""
    return HttpResponse('No statuses yet')
