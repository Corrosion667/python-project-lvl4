"""Admin module of Tasks app."""

from django.contrib import admin

from task_manager.tasks.models import Task

admin.site.register(Task)
