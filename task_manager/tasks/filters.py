
from django.forms import CheckboxInput
from django.utils.translation import gettext_lazy as _
from django_filters import BooleanFilter, FilterSet

from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    own_tasks = BooleanFilter(
        field_name='author',
        label=_('Show_own_tasks'),
        method='filter_own_tasks',
        widget=CheckboxInput,
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta (object):
        model = Task
        fields = [
            'status',
            'executor',
            'labels',
            'own_tasks',
        ]
