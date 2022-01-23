"""Forms for tasks app."""

from django.forms import ModelForm

from task_manager.tasks.models import Task
from django.utils.translation import gettext as _


class CreateForm(ModelForm):
    """Form for create tasks page."""

    class Meta(object):
        """Meta information of form."""

        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]
        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['status'].required = True
