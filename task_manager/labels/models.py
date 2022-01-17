"""Models for labels app."""

from django.db import models
from django.utils.translation import gettext_lazy as _

MAX_LENGTH_OF_LABEL_NAME = 30


class Label(models.Model):
    """Label for the task."""

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=MAX_LENGTH_OF_LABEL_NAME,
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Creation date'),
    )

    class Meta(object):
        """Meta information of model."""

        verbose_name = _('label')
        verbose_name_plural = _('labels')

    def __str__(self):
        """Present object as a string.

        Returns:
            Name of label.
        """
        return self.name
