"""Module for testing users app."""

from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

OK_CODE = 200
REDIRECT_CODE = 302


class UserTestCase(TestCase):
    """Test case class for users app."""

    def setUp(self):
        """Set up method for testing."""
        User.objects.create(
            username='test_user1',
            password='test_pass1',
        )
        protected_user = User.objects.create(
            username='test_user2',
            password='test_pass2',
        )
        test_status = Status.objects.create(
            name='test',
        )
        Task.objects.create(
            name='test',
            status=test_status,
            author=protected_user,
            executor=protected_user,
        )

    def test_signup_user(self):
        """Test for checking registration."""
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='signup.html')
        response = self.client.post(reverse('signup'), data={
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': 'test12345.',
            'password2': 'test12345.',
        },
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test', User.objects.get(pk=3).first_name)
        self.assertEqual('test', User.objects.get(pk=3).last_name)
        self.assertEqual('test', User.objects.get(pk=3).username)

    def test_user_updates_himself(self):
        """Test for checking how user can update himself."""
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('update_user', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='update_user.html')
        response = self.client.post(reverse('update_user', args='1'), data={
            'first_name': 'test_update',
            'last_name': 'test_update',
            'username': 'test_update',
            'password1': 'test12345.',
            'password2': 'test12345.',
        },
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_update', User.objects.get(pk=1).first_name)
        self.assertEqual('test_update', User.objects.get(pk=1).last_name)
        self.assertEqual('test_update', User.objects.get(pk=1).username)

    def test_user_updates_another(self):
        """Test for checking that user can not change other users."""
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('update_user', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'You do not have permission to change another user.',
        )
