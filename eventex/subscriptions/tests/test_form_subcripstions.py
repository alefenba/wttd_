from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form deve conter 4 campos """
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """ CPF deve conter apenas digitos"""
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form,'cpf','digits')
        #12345678901 1234 

    def test_cpf_has_11_digit(self):
        """CPF deve conter 11 digitos"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Nome deve estar formatado """
        # ALEFE GOMES -> Alefe Gomes
        form = self.make_validated_form(name="ALEFE GOMES")
        self.assertEqual('Alefe Gomes', form.cleaned_data['name'])


    def test_email_is_optional(self):
        """EMAIL é opcional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    
    def test_phone_is_optional(self):
        """Telefone é opcional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    
    def test_must_inform_email_or_phone(self):
        """Deve fornecer email ou telefone"""
        form = self.make_validated_form(email='',phone='')
        self.assertListEqual(['__all__'], list(form.errors))



    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)


    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors 
        errors_list=errors[field]
        self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid = dict(name='Alefe Gomes', cpf='12345678901',email='uchiha-itachi02@hotmail.com',phone='12-123456789')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
