from rest_framework import generics, permissions

from .models import Product
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser, FormParser


# This is for public access like stores home pages
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


# This is for private access like admin pages wich requires a authentication services middleware
class ProductViews(APIView):
    serializer_class = ProductSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (FormParser, MultiPartParser,)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data,
                    "message": "Produto cadastrado com sucesso!"
                }, 
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                "status": "error", 
                "data": serializer.errors,
                "message": "Não foi possivel cadastrar o produto."
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )
    #get list or get by id
    def get(self, request, id=None):
        if id:
            item = get_object_or_404(Product, id=id)
            serializer = ProductSerializer(item)
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data
                }, 
                status=status.HTTP_200_OK
            )

        items = Product.objects.all()
        serializer = ProductSerializer(items, many=True)
        return Response(
            {
                "status": "success", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )

    def patch(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success", 
                    "data": serializer.data,
                    "message": "Produto atualizado com sucesso!",
                }
            )
        else:
            return Response(
                {
                    "status": "error", 
                    "data": serializer.errors,
                    "message": "Não foi possivel deletar o produto",
                }
            )

    def delete(self, request, id=None):
        item = get_object_or_404(Product, id=id)
        item.delete()
        return Response(
            {
                "status": "success", 
                "data": "Item Deleted"
            }
        )