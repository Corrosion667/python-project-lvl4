from django.shortcuts import render


def index(request):
    """View for root site page."""
    return render(request, 'index.html', context={
        'who': 'World',
    })
