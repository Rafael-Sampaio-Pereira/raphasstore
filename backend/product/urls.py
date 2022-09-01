from django.urls import path, re_path

from . import views

app_name = "product"

group_actions = {"get": "list", "post": "create"}

single_actions = {
    "get": "retrieve",
    "put": "update",
    "patch": "partial_update",
    "delete": "destroy",
}
urlpatterns = [
    path("", views.ProductViews.as_view(group_actions),
         name='get_list_or_create_product'),
    re_path(r"^(?P<id>\d+)$", views.ProductViews.as_view(single_actions),
            name='manage_one_product'),
    path("all/", views.ProductListAPIView.as_view(), name="get_all_products"),
]
