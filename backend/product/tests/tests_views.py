from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from ..models import Product

class ProductViewTestCase(TestCase):
    
    def setUp(self) -> None:
        # store the password to login later
        password = 'admin123'
        # create super user to get access to the views
        my_admin = User.objects.create_superuser('admin', 'admin@test.com', password)
        _client = Client()
        # You'll need to log him in before you can send requests through the client
        _client.login(username=my_admin.username, password=password)
        # overrides TestCase client instance with our authenticated instance
        self.client = _client
        
        self.product = Product.objects.create(
            title = 'Application T-Shirt',
            brand = 'Dafiti',
            category = 'T-Shirt',
            description = 'Womans T-Shirt for tests propose only.',
            sku = '123456789',
            price = 29.90
        )

    def test_all_products_status_code_200(self):
        response = self.client.get(reverse('product:get_all_products'))
        self.assertEqual(200, response.status_code)
        
    def test_create_product_status_code_201(self):
        product_data = {   
            'title': 'White Soul T-Shirt',
            'brand': 'Dafiti',
            'category': 'T-Shirt',
            'description': 'Womans T-Shirt for tests propose only.',
            'sku': '123456789',
            'price': 29.90
        }
        response = self.client.post(
            reverse('product:get_list_or_create_product'), data=product_data)
        self.assertEqual(201, response.status_code)
    
    def test_create_product_status_code_400(self):
        product_data = {   
            'title': 'White Soul T-Shirt',
            'sku': '123456789',
        }
        response = self.client.post(
            reverse('product:get_list_or_create_product'), data=product_data)
        self.assertEqual(400, response.status_code)
    
    def test_partial_update_product_status_code_200(self):
        new_title = 'Changed Application T-Shirt'
        product_data = {   
            'title': new_title,
        }
        response = self.client.patch(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id}),
            data=product_data,
            content_type="application/json"
        )
        changed_title = response.__dict__['data']['data']['title']
        self.assertEqual(new_title, changed_title)
        self.assertEqual(200, response.status_code)
        
    def test_partial_update_product_status_code_400(self):
        product_data = {   
            'price': 'fashion week',
        }
        response = self.client.patch(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id}),
            data=product_data,
            content_type="application/json"
        )
        self.assertEqual(400, response.status_code)
        
    def test_retrive_product_status_code_200(self):
        response = self.client.get(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id}),
            content_type="application/json"
        )
        self.assertEqual(200, response.status_code)
        
    def test_delete_product_status_code_200(self):
        response = self.client.delete(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id}),
            content_type="application/json"
        )
        self.assertEqual(200, response.status_code)
    
    def test_update_product_status_code_200(self):
        product_data = {   
            'title': 'Mama Soul T-Shirt',
            'brand': 'Dafiti',
            'category': 'T-Shirt',
            'description': 'just a shirt.',
            'sku': '123456789',
            'price': 24.55
        }
        response = self.client.put(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id},
            ),
            content_type="application/json",
            data=product_data
        )
        self.assertEqual(200, response.status_code)
        
    def test_list_products_status_code_200(self):
        response = self.client.get(
            reverse('product:get_list_or_create_product'))
        self.assertEqual(200, response.status_code)
        
    
    def test_update_product_status_code_400(self):
        product_data = {   
            'title': 'Mama Soul T-Shirt',
        }
        response = self.client.put(
            reverse('product:manage_one_product',
                    kwargs={'id': self.product.id},
            ),
            content_type="application/json",
            data=product_data
        )
        self.assertEqual(400, response.status_code)
