"""URL routing of the project."""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('task_manager.users.urls')),
    path('labels/', include('task_manager.labels.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('admin/', admin.site.urls),
]
