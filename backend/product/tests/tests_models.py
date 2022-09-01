from django.test import TestCase
from ..models import Product, Inventory

class ProductModelTestCase(TestCase):
    
    def setUp(self) -> None:
        Product.objects.create(
            title = 'Black Soul T-Shirt',
            brand = 'Dafiti',
            category = 'T-Shirt',
            description = 'Mens T-Shirt for tests propose only.',
            sku = '123456789',
            price = 29.90
        )
    
    def test_str(self) :
        product = Product.objects.get(title = 'Black Soul T-Shirt')
        self.assertEquals(product.__str__(), 'Black Soul T-Shirt Dafiti')
        
class InventoryModelTestCase(TestCase):
    
    def setUp(self) -> None:
        self.product = Product.objects.create(
            title = 'White Soul T-Shirt',
            brand = 'Dafiti',
            category = 'T-Shirt',
            description = 'Womans T-Shirt for tests propose only.',
            sku = '123456789',
            price = 29.90
        )
        
        Inventory.objects.create(
            product = self.product,
            initial_quantity= 300,
            remaning_quantity = 200,
            profit_margin=30,
            purchase_price=9.99,
            size= 'G',
            color='red',
        )
    
    def test_str(self) :
        inventory = Inventory.objects.get(product = self.product)
        self.assertEquals(inventory.__str__(),
                          'White Soul T-Shirt Dafiti - 200')