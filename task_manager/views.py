from django.shortcuts import render


def main(request):
    """View for root site page."""
    return render(request, 'index.html', context={
        'who': 'World',
    })


def users(request):
    """View for users page."""
    return render(request, 'users.html')
