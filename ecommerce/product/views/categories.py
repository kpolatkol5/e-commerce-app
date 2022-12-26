
from django.views.generic import ListView, DetailView, TemplateView
from product.models.categories import Categories


class Categori_view(DetailView):
    model = Categories
    
    template_name = "products/categori/categories.html"

