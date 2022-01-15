"""Forms for users app."""

from django.contrib.auth.forms import UserCreationForm

from task_manager.users.models import User


class SignupForm(UserCreationForm):
    """Form for signup page."""

    class Meta(object):
        """Meta information of form."""

        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
