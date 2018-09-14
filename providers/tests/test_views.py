from rest_framework.test import APITestCase

from core.models import Language, Currency
from providers.models import Provider
from providers.serializers import ProviderSerializer


class PoviderListCreate(APITestCase):
    def setUp(self):
        self.language = Language.objects.create(id=1, name='English', code='en')
        self.currency = Currency.objects.create(id=1, name='Dollar', code='usd')
        dummy_data_1 = {
            'name': 'test1',
            'email': 'test1@test.com',
            'phone': '123-123',
            'language_id': 1,
            'currency_id': 1

        }
        dummy_data_2 = {
            'name': 'test2',
            'email': 'tes21@test.com',
            'phone': '123-123',
            'language_id': 1,
            'currency_id': 1

        }
        self.dummy_data_json = {
            'name': 'test_json',
            'email': 'test_json@test.com',
            'phone': '123-123',
            'language': 1,
            'currency': 1

        }
        Provider.objects.create(**dummy_data_1)
        Provider.objects.create(**dummy_data_2)

    def test_can_list(self):
        obj_list = Provider.objects.all()
        response = self.client.get('/providers/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data, ProviderSerializer(obj_list, many=True).data)
        self.assertEqual(len(ProviderSerializer(obj_list, many=True).data), 2)

    def test_can_create(self):
        response = self.client.post('/providers/', self.dummy_data_json)
        obj = Provider.objects.filter(name='test_json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(obj), 1)
        self.assertEqual(response.data, ProviderSerializer(obj[0]).data)


class ProviderRetrieveUpdateDestroy(APITestCase):
    def setUp(self):
        self.language = Language.objects.create(id=1, name='English', code='en')
        self.currency = Currency.objects.create(id=1, name='Dollar', code='usd')
        dummy_data_1 = {
            'id': 1,
            'name': 'test1',
            'email': 'test1@test.com',
            'phone': '123-123',
            'language_id': 1,
            'currency_id': 1

        }

        self.dummy_data_json = {
            'name': 'test_json',
            'email': 'test_json@test.com',
            'phone': '123-123',
            'language': 1,
            'currency': 1

        }
        Provider.objects.create(**dummy_data_1)

    def test_can_retrieve(self):
        obj_list = Provider.objects.get(pk=1)
        response = self.client.get('/providers/1/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(response.data, ProviderSerializer(obj_list).data)

    def test_can_update(self):
        old_obj = Provider.objects.get(pk=1)
        response = self.client.put('/providers/1/', self.dummy_data_json)
        new_obj = Provider.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(old_obj.name, new_obj.name)

    def test_can_delete(self):
        before_delete_obj = Provider.objects.filter(pk=1).exists()
        response = self.client.delete('/providers/1/')
        after_delete_obj = Provider.objects.filter(pk=1).exists()
        self.assertEqual(response.status_code, 204)
        self.assertNotEqual(before_delete_obj, after_delete_obj)
