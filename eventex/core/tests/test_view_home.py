from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    fixtures = ['keynotes.json']
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

    
    def test_speaker(self):
        """Deve mostrar os palestrantes chaves"""

        contents = ['href="{}"'.format(r('speaker_detail', slug = 'grace-hopper')),
        'Grace Hopper',
        'http://hbn.link/hopper-pic',
        'href="{}"'.format(r('speaker_detail', slug = 'alan-turing')),
        'Alan Turing', 
        'http://hbn.link/turing-pic',]
        
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.response, expected)


    def test_talks_link(self):
        expected = 'href="{}"'.format(r('talk_list'))
        self.assertContains(self.response, expected)