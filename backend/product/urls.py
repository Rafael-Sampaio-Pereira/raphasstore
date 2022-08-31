from django.urls import path, re_path
from . import views

app_name = 'product'

single_actions = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
}
urlpatterns = [
    path('', views.ProductViews.as_view()),
    re_path(r'^(?P<id>\d+)$', views.ProductViews.as_view()),
    re_path(
        'list/', views.ProductListAPIView.as_view(),
        name='product-list'
    )
]
