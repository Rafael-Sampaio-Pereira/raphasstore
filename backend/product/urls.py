from django.urls import path, re_path
from . import views

app_name = 'product'

single_actions = {
    'get': 'retrieve',
    # 'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    'post': 'create'
}
urlpatterns = [
    path('', views.ProductViews.as_view(single_actions)),
    re_path(r'^(?P<id>\d+)$', views.ProductViews.as_view(single_actions)),
    path(
        'list/', views.ProductListAPIView.as_view(),
        name='product-list'
    )
]
