from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ecommerce.settings import LOGIN_URL
# model import
from core.models.slider import Slider
from product.models.categories import Categories


class Base_view(LoginRequiredMixin, UserPassesTestMixin):
    login_url = LOGIN_URL  # doğru çalışıyor mu emin değilim

    # redirect_field_name = 'redirect_to'

    # def test_func(self):
    # return self.request.user.email.endswith('@example.com')

    # def handle_no_permission(self):
    # return redirect(LOGIN_URL)


class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by("-id")[:5]
        context["new_produt_categori"] = Categories.objects.exclude(
            parent=None
        )
        return context
