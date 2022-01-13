from django.urls import path

from task_manager.users.views import UsersListView

urlpatterns = [
    path('', UsersListView.as_view(), name='users'),
]
