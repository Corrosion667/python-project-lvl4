from django.urls import path

from task_manager.users.views import LoginView, MainPageView, UsersListView, SignupView

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('users/create/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LoginView.as_view(), name='logout'),
    path('users/', UsersListView.as_view(), name='users'),
]
