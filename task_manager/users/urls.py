from django.urls import path

from task_manager.users.views import (
    MainPageView,
    SignupView,
    UserLoginView,
    UserLogoutView,
    UsersListView,
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('users/create/', SignupView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', UsersListView.as_view(), name='users'),
]
