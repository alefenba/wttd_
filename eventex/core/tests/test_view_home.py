from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ GET / deve retornar 200 """
        response = self.client.get('/')
        self.assertEqual(200, self.response.status_code)
    
    
    def test_template(self):
        """Deve utilizar index.html"""
        response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')