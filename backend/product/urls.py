from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductViews.as_view()),
    path('<int:id>', views.ProductViews.as_view()),
    path(
        'list/', views.ProductListAPIView.as_view(),
        name='product-list'
    )
]
