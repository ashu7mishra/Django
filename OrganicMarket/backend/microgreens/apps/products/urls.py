from django.urls import path
from .views import ProductListView, ProductDetailsView


urlpattern = [
    path("", ProductListView.as_view(), name='product-list'),
    path("", ProductDetailsView.as_view(), name='product-detail'),
]