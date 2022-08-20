from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic',
        )

    def test_email(self):
        contact = Contact.objects.create(speaker = self.speaker, kind=Contact.EMAIL, value='henrique@bastos.net')
        self.assertTrue(Contact.objects.exists())
    
    
    def test_telefone(self):
        contact = Contact.objects.create(speaker = self.speaker, kind=Contact.PHONE, value='21-996186180')
        self.assertTrue(Contact.objects.exists())

    
    def test_choices(self):
        """Contato deve ser limitado a E ou P """
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError,contact.full_clean)

    
    def test_str(self):
        contact = Contact.objects.create(speaker = self.speaker, kind=Contact.EMAIL , value='henrique@bastos.net')
        self.assertEqual('henrique@bastos.net',str(contact))

    
class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name ='Alefe Gomes',
            slug='alefe-gomes',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='uchiha-itachi02@hotmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='12-123456789')


    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['uchiha-itachi02@hotmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    
    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['12-123456789']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
