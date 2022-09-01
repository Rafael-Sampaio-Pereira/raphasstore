from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

MODEL_CLASS = Product
SERIALIZER_CLASS = ProductSerializer
CLASS_NAME = MODEL_CLASS._meta.verbose_name.title()


def create(request):
    serializer = SERIALIZER_CLASS(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data,
                "message": f"{CLASS_NAME}: Cadastrado realizado com sucesso!",
            },
            status=status.HTTP_201_CREATED,
        )
    else:
        return Response(
            {
                "status": "error",
                "data": serializer.errors,
                "message": (
                    f"{CLASS_NAME}: Não foi possível realizar o cadastro."
                ),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


def get_one(id):
    item = get_object_or_404(MODEL_CLASS, id=id)
    serializer = SERIALIZER_CLASS(item)
    return Response(
        {"status": "success", "data": serializer.data, "message": None},
        status=status.HTTP_200_OK,
    )


def get_list(request):
    items = Product.objects.all()
    serializer = SERIALIZER_CLASS(items, many=True)
    return Response(
        {"status": "success", "data": serializer.data, "message": None},
        status=status.HTTP_200_OK,
    )


def destroy(id):
    item = get_object_or_404(MODEL_CLASS, id=id)
    item.delete()
    return Response(
        {
            "status": "success",
            "data": None,
            "message": f"{CLASS_NAME}: Item deletado com sucesso.",
        },
        status=status.HTTP_200_OK
    )


def partial_update(request, id):
    item = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(
        instance=item,
        data=request.data,
        partial=True
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data,
                "message": f"{CLASS_NAME}: Atualização realizada com sucesso!",
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                "status": "error",
                "data": serializer.errors,
                "message": (
                    f"{CLASS_NAME}: Não foi possível realizar a atualização."
                ),
            },
            status=status.HTTP_400_BAD_REQUEST
        )


def full_update(request, id):
    item = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(
        instance=item,
        data=request.data,
        partial=False
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            {
                "status": "success",
                "data": serializer.data,
                "message": f"{CLASS_NAME}: Atualização realizada com sucesso!",
            },
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {
                "status": "error",
                "data": serializer.errors,
                "message": (
                    f"{CLASS_NAME}: Não foi possível realizar a atualização."
                ),
            },
            status=status.HTTP_400_BAD_REQUEST
        )
