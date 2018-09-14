from unittest import TestCase

from core.models import Language, Currency


class LanguageTestCase(TestCase):
    def setUp(self):
        self.name = 'Test'
        self.code = 'T'

    def test_add_record_to_language(self):
        obj = Language.objects.create(name=self.name, code=self.code)

        self.assertTrue(isinstance(obj, Language))
        self.assertEqual(obj.__str__(), '{}'.format(obj.name))
        self.assertEqual(obj.name, self.name)
        self.assertEqual(obj.code, self.code)


class CurrencyTestCase(TestCase):
    def setUp(self):
        self.name = 'Test'
        self.code = 'T'

    def test_add_record_to_currency(self):
        obj = Currency.objects.create(name=self.name, code=self.code)

        self.assertTrue(isinstance(obj, Currency))
        self.assertEqual(obj.__str__(), '{}'.format(obj.name))
        self.assertEqual(obj.name, self.name)
        self.assertEqual(obj.code, self.code)
