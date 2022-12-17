from django.urls import path
from product.views.products import ProductListView, ProductDetailView

urlpatterns = [
    path("store/", ProductListView.as_view(), name="product-list"),
    path("store/products/<slug:slug>/",
         ProductDetailView.as_view(), name="product-details"),
]
