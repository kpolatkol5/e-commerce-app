from django.views.generic import ListView, DetailView
from product.models.products import Products


class ProductListView(ListView):
    queryset = Products.objects.filter(is_active=True, stock__gt=0)
    template_name = "products/product_list.html"


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"
