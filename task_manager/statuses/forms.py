from django.forms import ModelForm
from task_manager.statuses.models import Status


class CreateForm(ModelForm):
    class Meta:
        model = Status
        fields = ['name']
