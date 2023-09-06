'''
test for the Django admin modification
'''

from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSitetest(TestCase):
    '''Test for django admin'''
    def setUp(self):
        '''create user and client'''
        # create client to simulate http request
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='adminuser@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        '''user are listed on page.'''
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)
        self.assertContains(response, self.admin_user.email)

    def test_edit_user_page(self):
        '''test edit user page'''
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_ceate_user_page(self):
        '''test user creation page works'''
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
