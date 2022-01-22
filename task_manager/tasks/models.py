"""Models for tasks app."""

from django.db import models
from django.utils.translation import gettext as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User

MAX_LENGTH_OF_TASK_NAME = 80
MAX_LENGTH_OF_TASK_DESCRIPTION = 500


class Task(models.Model):
    """Model of task objects."""

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=MAX_LENGTH_OF_TASK_NAME,
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Creation date'),
    )
    description = models.TextField(
        verbose_name=_('Description'),
        max_length=MAX_LENGTH_OF_TASK_DESCRIPTION,
        blank=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Status'),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Author'),
        related_name=('tasks'),
    )
    executor = models.ForeignKey(
        User,
        verbose_name=_('Executor'),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        # related_name=_('tasks'),
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name=_('Labels'),
        blank=True,
        related_name=('tasks'),
        through='TaskLabelRelation',
        through_fields=('task', 'label'),
    )

    def __str__(self):
        """Present object as a string.

        Returns:
            Name of task.
        """
        return self.name


class TaskLabelRelation(models.Model):
    task = models.ForeignKey(
        Task,
        on_delete=models.PROTECT,
    )
    label = models.ForeignKey(
        Label,
        on_delete=models.PROTECT,
    )
