"""Statuses app config file."""

from django.apps import AppConfig


class StatusesConfig(AppConfig):
    """Application config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager.statuses'
