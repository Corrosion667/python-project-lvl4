from django.shortcuts import render


def users(request):
    """View for users page."""
    return render(request, 'users.html')
