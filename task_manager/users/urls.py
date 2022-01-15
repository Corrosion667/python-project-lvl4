"""URL routing of the users app."""

from django.urls import path

from task_manager.users.views import (
    DeleteUserView,
    MainPageView,
    SignupView,
    UpdateUserView,
    UserLoginView,
    UserLogoutView,
    UsersListView,
)

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('users/', UsersListView.as_view(), name='users'),
    path('users/create/', SignupView.as_view(), name='signup'),
    path(
        'users/<int:pk>/update/',
        UpdateUserView.as_view(),
        name='update_user',
    ),
    path(
        'users/<int:pk>/delete/',
        DeleteUserView.as_view(),
        name='delete_user',
    ),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
