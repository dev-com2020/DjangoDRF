from rest_framework import status
from rest_framework.test import APITestCase


class BasicTests(APITestCase):
    def test_basic_req(self):
        url = '/api/hello/'
        expected_data = {'msg': 'metoda jest ok'}
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
