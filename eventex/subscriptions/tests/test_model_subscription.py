from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(name="Alefe Gomes", cpf="12345678901",email="uchiha-itachi02@hotmail.com",phone="12-992179305")
        self.obj.save()
    
    def test_create(self):
        self.assertTrue(Subscription.objects.exists())


    def test_created_at(self):
        """Subscription deve ter uma created_at attr automatico."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Alefe Gomes', str(self.obj))