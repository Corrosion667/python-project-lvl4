from django.apps import AppConfig


class UsersConfig(AppConfig):
    """Application config."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'task_manager.users'
    label = 'users'
