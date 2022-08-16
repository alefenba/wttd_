import mailbox
import unittest
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from django.shortcuts import resolve_url as r 

from eventex.subscriptions.models import Subscription


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """GET /inscricao/ deve retornar status code 200"""
        self.assertEqual(200,self.resp.status_code)

    
    def test_template(self):
        """ Deve retornar subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """ html deve contar tags de input """
        tags = (('<form', 1),('<input', 6),('type="text" ', 3),('type="submit" ', 1))
        
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """ html deve conter csrf """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context deve ter subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)



class SubscriptionsNewPost(TestCase):
    def setUp(self):
        data = dict(name='Alefe Gomes', cpf='12345678901', email='uchiha-itachi02@hotmail.com', phone='12-123456789')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.hash_id=Subscription.objects.first().hash_id
    
    
    def test_post(self):
        """POST válido deve redirecionar /inscricao/id/"""
        self.assertRedirects(self.resp, r('subscriptions:detail',self.hash_id))
        

    def test_send_subscribe_emails(self):
        self.assertEquals(1, len(mail.outbox))

    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())


class SubscriptionsNewInvalidPost(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """ POST invalido não deve redirecionar """
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())

class TemplateRegression(TestCase):
    def test_template_has_non_field_errors(self):
        invalid_data = dict(name='Alefe Gomes', cpf='12345678901')
        response = self.client.post(r('subscriptions:new'), invalid_data)
        self.assertContains(response, '<ul class="errorlist nonfield">')
