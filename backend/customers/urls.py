from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path(
        '', views.CustomerListAPIView.as_view(),
        name='customer-list'
    )
]
