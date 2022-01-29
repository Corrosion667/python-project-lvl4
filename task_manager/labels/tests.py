"""Module for testing labels app."""

from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

OK_CODE = 200
REDIRECT_CODE = 302


class LabelTestCase(TestCase):
    """Test case class for statuses app."""

    def setUp(self):
        """Set up method for testing."""
        test_user = User.objects.create(
            username='test_user',
            password='test_pass',
        )
        test_status = Status.objects.create(
            name='test',
        )
        test_label = Label.objects.create(
            name='test_label1',
        )
        test_task = Task.objects.create(
            name='test',
            status=test_status,
            author=test_user,
        )
        test_task.labels.add(test_label)
        self.client.force_login(test_user)

    def test_labels_list(self):
        """Test for checking labels page."""
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='labels.html')
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Label.objects.all(),
            ordered=False,
        )

    def test_create_label(self):
        """Test for checking label creation."""
        response = self.client.get(reverse('create_label'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='create_label.html')
        response = self.client.post(reverse('create_label'), data={
            'name': 'test_label2',
        },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Label successfully created',
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_label2', Label.objects.get(pk=2).name)

    def test_update_label(self):
        """Test for checking how label can be updated."""
        response = self.client.get(reverse('update_label', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='update_label.html')
        response = self.client.post(reverse('update_label', args='1'), data={
            'name': 'test_update',
        },
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Label successfully changed',
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_update', Label.objects.get(pk=1).name)

    def test_delete_label(self):
        """Test for checking how label can be deleted."""
        Label.objects.create(
            name='test_label2',
        )
        response = self.client.get(reverse('delete_label', args='2'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='delete_label.html')
        response = self.client.post(reverse('delete_label', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Label successfully deleted',
        )
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=2)

    def test_delete_busy_label(self):
        """Test for checking that label in use can not be deleted."""
        response = self.client.post(reverse('delete_label', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]),
            'Can not delete label because it is in use',
        )
