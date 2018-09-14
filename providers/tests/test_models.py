from unittest import TestCase

from core.models import Language, Currency
from providers.models import Provider


class ProviderTestCase(TestCase):
    def setUp(self):
        self.name = 'Test'
        self.email = 'test@test.com'
        self.phone = '1234-123'

        self.language = Language.objects.create(name='language', code='lang_code')
        self.currency = Currency.objects.create(name='currency', code='cur_code')

    def test_add_record_to_provider(self):
        obj = Provider.objects.create(name=self.name, email=self.email, phone=self.phone, language=self.language,
                                      currency=self.currency)

        self.assertTrue(isinstance(obj, Provider))
        self.assertEqual(obj.__str__(), '{}'.format(obj.name))
        self.assertEqual(obj.name, self.name)
        self.assertEqual(obj.email, self.email)
        self.assertEqual(obj.phone, self.phone)
        self.assertEqual(obj.language, self.language)
        self.assertEqual(obj.currency, self.currency)
