from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('home'))

    def test_get(self):
        """ GET / deve retornar 200 """
        response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)
    
    
    def test_template(self):
        """Deve utilizar index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.response, expected)