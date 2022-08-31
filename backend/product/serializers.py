from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'category', 'price', 'description', 'image', 'brand')
        read_only_fields = ('id',)
