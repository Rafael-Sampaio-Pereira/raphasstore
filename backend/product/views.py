from rest_framework import generics, permissions

from .models import Product
from .serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
