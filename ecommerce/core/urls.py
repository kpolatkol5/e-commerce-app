from django.urls import path
from core.views.index import HomePageView
from core.views.htmx import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home-page"),
]


htmx_patterns = [
    path("product", htmx_modal_product, name="htmx_product"),
]


urlpatterns += htmx_patterns
