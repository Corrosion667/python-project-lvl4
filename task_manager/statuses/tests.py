"""Module for testing statuses app."""

from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

OK_CODE = 200
REDIRECT_CODE = 302


class StatusTestCase(TestCase):
    """Test case class for statuses app."""

    def setUp(self):
        """Set up method for testing."""
        test_user = User.objects.create(
            username='test_user',
            password='test_pass',
        )
        test_status = Status.objects.create(
            name='test_status1',
        )
        Task.objects.create(
            name='test',
            status=test_status,
            author=test_user,
        )
        self.client.force_login(test_user)

    def test_statuses_list(self):
        """Test for checking statuses page."""
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='statuses.html')
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Status.objects.all(),
            ordered=False,
        )

    def test_create_status(self):
        """Test for checking status creation."""
        response = self.client.get(reverse('create_status'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='create_status.html')
        response = self.client.post(reverse('create_status'), data={
            'name': 'test_status2',
        },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Status successfully created',
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_status2', Status.objects.get(pk=2).name)

    def test_update_status(self):
        """Test for checking how status can be updated."""
        response = self.client.get(reverse('update_status', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='update_status.html')
        response = self.client.post(reverse('update_status', args='1'), data={
            'name': 'test_update',
        },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Status successfully changed',
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_update', Status.objects.get(pk=1).name)

    def test_delete_status(self):
        """Test for checking how status can be deleted."""
        Status.objects.create(
            name='test_status2',
        )
        response = self.client.get(reverse('delete_status', args='2'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='delete_status.html')
        response = self.client.post(reverse('delete_status', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Status successfully deleted',
        )
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=2)

    def test_delete_busy_status(self):
        """Test for checking that status in use can not be deleted."""
        response = self.client.post(reverse('delete_status', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Can not delete status because it is in use',
        )
