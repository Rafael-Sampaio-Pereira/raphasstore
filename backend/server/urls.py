"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from drf_spectacular.views import (
#     SpectacularAPIView,
#     SpectacularRedocView,
#     SpectacularSwaggerView,
# )
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

# Configure titles
admin.site.site_header = "RaphasStore"
admin.site.site_title = "RaphasStore | Painel Administrativo"
admin.site.index_title = "Painel Administrativo"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/product/", include("product.urls", namespace='product')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# JWTAuthentication
urlpatterns += [
    path("api/token/",
         TokenObtainPairView.as_view(), name="token_obtain_view"),
    path("api/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh_view"),
]


# ==========================[ DOCUMENTATION URLS ]========================

# There is no possible to use more than one default schemas class same time
# in django, so we have to choose CoreAPI or Spetacular/Swagger.

# CoreAPI Documentantion and API interactions
# PS: To use CoreAPI documentation, place bellow at the end of settings.py:
# REST_FRAMEWORK = {
#   'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
# }
urlpatterns += [
    path("api/docs/", include_docs_urls(title="RaphasStoreAPI")),
    path(
        "api/schema/",
        get_schema_view(
            title="RaphasStore",
            description="API for the RaphasStore",
            version="1.0.0"
        ),
        name="openapi-schema",
    ),
]

# Spetacular and Swagger urls
# PC: To use Swagger/Spetacular docs, place bellow at the end of settings.py:
# REST_FRAMEWORK = {
#   'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
# }
#
# urlpatterns += [
#     path('api/yaml_schema/', SpectacularAPIView.as_view(), name='schema'),
#     path('api/swagger/',
#          SpectacularSwaggerView.as_view(url_name='schema'),
#          name='swagger-ui'
#     ),
#     path('api/redoc/',
#           SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]
