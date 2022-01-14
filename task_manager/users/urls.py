from django.urls import path

from task_manager.users.views import LoginView, MainPageView, UsersListView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UsersListView.as_view(), name='users'),
]
