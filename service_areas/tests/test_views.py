import json

from django.contrib.gis.geos import Polygon, Point
from rest_framework.test import APITestCase

from core.models import Language, Currency
from providers.models import Provider
from service_areas.models import ServiceArea
from service_areas.serializers import ServiceAreaSerializer


class PoviderListCreate(APITestCase):
    def setUp(self):
        self.area_json = {"type": "Polygon",
                          "coordinates": [[[0.0, 0.0], [4.0, 0.0], [4.0, 4.0], [4.0, 0.0], [0.0, 0.0]]]}
        dummy_data_provider = {
            'id': 1,
            'name': 'test1',
            'email': 'test1@test.com',
            'phone': '123-123',
            'language': Language.objects.create(name='language', code='lang_code'),
            'currency': Currency.objects.create(name='currency', code='cur_code'),

        }
        dummy_data_1 = {
            'name': 'test1',
            'price': 1000.00,
            'area': Polygon(((5.0, 5.0), (5.0, 10.0), (10.0, 10.0), (10.0, 5.0), (5.0, 5.0))),
            'provider_id': 1,

        }
        dummy_data_2 = {
            'name': 'test2',
            'price': 10000.00,
            'area': Polygon(((0.0, 0.0), (0.0, 5.0), (5.0, 5.0), (5.0, 0.0), (0.0, 0.0))),
            'provider_id': 1,

        }
        self.dummy_data_json = {
            'name': 'test_json',
            'price': 10000.00,
            'area': self.area_json,
            'provider': 1,

        }

        self.provider = Provider.objects.create(**dummy_data_provider)
        ServiceArea.objects.create(**dummy_data_1)
        ServiceArea.objects.create(**dummy_data_2)

    def test_can_list(self):
        obj_list = ServiceArea.objects.all()
        response = self.client.get('/service-areas/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data, ServiceAreaSerializer(obj_list, many=True).data)
        self.assertEqual(len(ServiceAreaSerializer(obj_list, many=True).data), 2)

    def test_can_list_with_filters(self):
        obj_list = ServiceArea.objects.filter(area__contains=Point(1.0, 1.0))
        response = self.client.get('/service-areas/?lat=1&lng1', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(ServiceAreaSerializer(obj_list, many=True).data['features']), 1)

    def test_can_create(self):
        response = self.client.post('/service-areas/', json.dumps(self.dummy_data_json),
                                    content_type='application/json')
        obj = ServiceArea.objects.filter(name='test_json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(obj), 1)
        self.assertEqual(response.data, ServiceAreaSerializer(obj[0]).data)


class ServiceAreaRetrieveUpdateDestroy(APITestCase):
    def setUp(self):
        self.area_json = {"type": "Polygon",
                          "coordinates": [[[0.0, 0.0], [4.0, 0.0], [4.0, 4.0], [4.0, 0.0], [0.0, 0.0]]]}
        dummy_data_provider = {
            'id': 1,
            'name': 'test1',
            'email': 'test1@test.com',
            'phone': '123-123',
            'language': Language.objects.create(name='language', code='lang_code'),
            'currency': Currency.objects.create(name='currency', code='cur_code'),

        }
        self.dummy_data_1 = {
            'id': 1,
            'name': 'test1',
            'price': 1000.00,
            'area': Polygon(((5.0, 5.0), (5.0, 10.0), (10.0, 10.0), (10.0, 5.0), (5.0, 5.0))),
            'provider_id': 1,

        }

        self.dummy_data_json = {
            'name': 'test_json',
            'price': 10000.00,
            'area': self.area_json,
            'provider': 1,

        }

        self.provider = Provider.objects.create(**dummy_data_provider)
        ServiceArea.objects.create(**self.dummy_data_1)

    def test_can_retrieve(self):
        obj = ServiceArea.objects.get(pk=1)
        response = self.client.get('/service-areas/1/', content_type='application/json')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data, ServiceAreaSerializer(obj).data)

    def test_can_update(self):
        old_obj = ServiceArea.objects.get(pk=1)
        response = self.client.put('/service-areas/1/', json.dumps(self.dummy_data_json),
                                   content_type='application/json')
        new_obj = ServiceArea.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(old_obj.name, new_obj.name)

    def test_can_delete(self):
        old_obj = ServiceArea.objects.filter(pk=1).exists()
        response = self.client.delete('/service-areas/1/', content_type='application/json')
        new_obj = ServiceArea.objects.filter(pk=1).exists()
        self.assertEqual(response.status_code, 204)
        self.assertNotEqual(old_obj, new_obj)
