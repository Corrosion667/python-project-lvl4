"""Forms for labels app."""

from django.forms import ModelForm

from task_manager.labels.models import Label


class CreateForm(ModelForm):
    """Form for create label page."""

    class Meta(object):
        """Meta information of form."""

        model = Label
        fields = ['name']
