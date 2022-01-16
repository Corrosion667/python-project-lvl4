"""URL routing of the tasks app."""

from django.urls import path

from task_manager.tasks import views

urlpatterns = [
    path('', views.main, name='tasks'),
]
