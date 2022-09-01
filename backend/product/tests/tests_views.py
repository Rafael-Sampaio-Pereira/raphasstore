from urllib import response
from django.test import TestCase
from django.urls import reverse

class ProductViewTestCase(TestCase):

    def test_all_products_status_code_200(self):
        response = self.client.get(reverse('product:all'))
        self.assertEqual(200, response.status_code)