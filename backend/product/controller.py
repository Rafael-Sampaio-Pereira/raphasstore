from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

MODEL_CLASS = Product
SERIALIZER_CLASS = ProductSerializer

def create(request):
    serializer = SERIALIZER_CLASS(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success", 
                "data": serializer.data,
                "message": f"{MODEL_CLASS.__name__} cadastrado com sucesso!"
            }, 
            status=status.HTTP_201_CREATED
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
        
def retrieve_one_or_list(id):
    if id:
        item = get_object_or_404(MODEL_CLASS, id=id)
        serializer = SERIALIZER_CLASS(item)
        return Response(
            {
                "status": "success", 
                "data": serializer.data
            }, 
            status=status.HTTP_200_OK
        )

    items = Product.objects.all()
    serializer = SERIALIZER_CLASS(items, many=True)
    return Response(
        {
            "status": "success", 
            "data": serializer.data
        }, 
        status=status.HTTP_200_OK
    )
    

def destroy(id):
    item = get_object_or_404(MODEL_CLASS, id=id)
    item.delete()
    return Response(
        {
            "status": "success", 
            "data": f"{MODEL_CLASS.__name__} deletado"
        }
    )
def partial_update(request, id): 
    item = get_object_or_404(Product, id=id)
    # item = Product.objects.get(pk=id)
    serializer = ProductSerializer(instance=item, data=request.data, partial=True)
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