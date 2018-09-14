from unittest import TestCase

from django.contrib.gis.geos import Polygon

from core.models import Language, Currency
from providers.models import Provider
from service_areas.models import ServiceArea


class ServiceAreaTestCase(TestCase):
    def setUp(self):
        self.name = 'Test'
        self.price = 1.50
        self.area = Polygon()

        language = Language.objects.create(name='language', code='lang_code')
        currency = Currency.objects.create(name='currency', code='cur_code')
        self.provider = Provider.objects.create(name='test', email='test@test.com', phone='123', language=language,
                                                currency=currency)

    def test_add_record_to_service_area(self):
        obj = ServiceArea.objects.create(name=self.name, price=self.price, area=self.area,
                                         provider=self.provider)

        self.assertTrue(isinstance(obj, ServiceArea))
        self.assertEqual(obj.__str__(), '{}'.format(obj.name))
        self.assertEqual(obj.name, self.name)
        self.assertEqual(obj.price, self.price)
        self.assertEqual(obj.area, self.area)
        self.assertEqual(obj.provider, self.provider)
