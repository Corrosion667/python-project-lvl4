"""Models for statuses app."""

from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_LENGTH_OF_STATUS_NAME = 50


class Status(models.Model):
    """Status of the task."""

    name = models.CharField(
        verbose_name=_('AAAA'),
        max_length=MAX_LENGTH_OF_STATUS_NAME,
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Creation date'),
    )

    def __str__(self):
        """Present object as a string.

        Returns:
            Name of status.
        """
        return self.name
