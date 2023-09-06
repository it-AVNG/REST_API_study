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
        #crete client to simulate http request
        self.client=Client()
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
        result = self.client.get(url)

        self.assertContains(result, self.user.name)
        self.assertContains(result, self.user.email)
        self.assertContains(result, self.admin_user.email)
