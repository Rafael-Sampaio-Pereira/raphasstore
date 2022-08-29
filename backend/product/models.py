from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    brand = models.CharField(null=True, blank=True, max_length=100)
    sku = models.CharField(null=True, blank=True, max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='media')
    price = models.FloatField(null=False, blank=False)
    purchase_price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title', 'description', 'brand',  'sku', 'category', 'purchase_price', 'price', 'image']

    def __str__(self):
        return f'{self.title} {str(self.brand)}'