from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    """View for labels main page."""
    return HttpResponse('No labels yet')
