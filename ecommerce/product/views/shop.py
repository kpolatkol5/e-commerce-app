from django.views.generic import ListView, DetailView, TemplateView
from product.models.products import Products
from product.models.product_option import Option

from core.views.index import Base_view


class ProductListView(TemplateView):
    template_name = "products/product_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Products.objects.filter(is_active=True)
        context['product_count'] = Products.objects.filter(is_active=True).count()
        context['option'] = Option.objects.filter(is_active = True)
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = "products/product_detail.html"
