from rest_framework import generics, mixins, permissions, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .controllers import (create, destroy, full_update, get_list, get_one,
                          partial_update)
from .models import Product
from .serializers import ProductSerializer


# This is for public access like stores home pages
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()


# This is for private access like admin pages wich requires a
# authentication services middleware
class ProductViews(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductSerializer
    authentication_classes = (
        JWTAuthentication,
        BasicAuthentication,
        SessionAuthentication,
    )
    permission_classes = (IsAuthenticated,)
    parser_classes = (
        FormParser,
        MultiPartParser,
        JSONParser,
    )
    queryset = ''

    # This overrides the UpdateModelMixin update method and enable the partial
    # update
    # def update(self, request, *args, **kwargs):
    #     kwargs["partial"] = True
    #     return super().update(request, *args, **kwargs)

    def create(self, request):
        return create(request)

    # get list or get by id
    def retrieve(self, request, id=None):
        return get_one(id)

    def partial_update(self, request, id=None):
        return partial_update(request, id)

    # UpdateModelMixin already have a update method, so we need another name
    def update(self, request, id=None):
        return full_update(request, id)

    def destroy(self, request, id=None):
        return destroy(id)

    def list(self, request):
        return get_list(request)
