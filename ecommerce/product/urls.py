from django.urls import path
from product.views.shop import ProductListView, ProductDetailView
from product.views.categories import Categori_view


urlpatterns = [
    path("store/", ProductListView.as_view(), name="product-list"),
    path("store/products/<slug:slug>/",ProductDetailView.as_view(), name="product-details"),
    path('store/categories/<slug:slug>' , Categori_view.as_view()  , name="categori")
]
