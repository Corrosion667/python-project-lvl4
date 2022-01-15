from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.Model):
    name = models.CharField(
        verbose_name=_('Name'), max_length=50, unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_('Creation date'),
    )

    class Meta:
        verbose_name = _('status')
        verbose_name_plural = _('statuses')

    def __str__(self):
        return self.name
