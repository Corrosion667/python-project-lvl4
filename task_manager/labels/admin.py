"""Admin module of Labels app."""

from django.contrib import admin

from task_manager.labels.models import Label

admin.site.register(Label)
