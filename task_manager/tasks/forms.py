"""Forms for tasks app."""

from django.forms import ModelForm

from task_manager.tasks.models import Task


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['status'].required = True
