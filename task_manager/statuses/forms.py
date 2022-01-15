"""Forms for statuses app."""

from django.forms import ModelForm

from task_manager.statuses.models import Status


class CreateForm(ModelForm):
    """Form for create status page."""

    class Meta(object):
        """Meta information of form."""

        model = Status
        fields = ['name']
