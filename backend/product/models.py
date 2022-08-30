from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    brand = models.CharField(null=True, blank=True, max_length=100)
    sku = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = [
            'title',
            'description',
            'brand',
            'sku',
            'category',
            'price',
            'image'
        ]

    def __str__(self):
        return f'{self.title} {str(self.brand)}'
    

class Inventory(models.Model):
    product = models.ForeignKey(
        "Product",
        related_name="Product_Inventory",
        on_delete=models.CASCADE
    )
    initial_quantity = models.IntegerField(null=False, blank=False)
    purchase_price = models.FloatField(null=False, blank=False)
    remaning_quantity = models.IntegerField(null=False, blank=False)
    profit_margin = models.IntegerField(null=False, blank=False)
    size = models.CharField(max_length=5, null=True, blank=True,)
    color = models.CharField(max_length=100, null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = [
            'product',
            'initial_quantity',
            'remaning_quantity',
            'purchase_price',
            'profit_margin',
            'color',
            'size',
            'updated_at'
        ]

    def __str__(self):
        return f'{self.product.title} {str(self.product.brand)} - {self.remaning_quantity}'
