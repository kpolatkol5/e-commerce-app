from django.shortcuts import render
from django.views.generic import TemplateView
from core.models.slider import Slider



def anasayfa(request):
    return render(request , "core/index.html" , context={"data":"data"} )


class HomePageView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.all().order_by("-id")[:5]
        return context
    