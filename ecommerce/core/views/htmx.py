from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from product.models.products import Products
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core import serializers


# @method_decorator(csrf_exempt)
# def htmx_modal_product(request):

#     product_id = request.POST["product_id"]
#     print(product_id)
#     data = Products.objects.values()
#     for i in data:
#         if i["id"] == int(product_id):
#             result = i["id"]
#             print(i)

#     result = result
#     return JsonResponse(data=data, safe=False)


@method_decorator(csrf_exempt)
def htmx_modal_product(request):

    product_id = request.POST["product_id"]

    product = Products.objects.get(id=product_id)

    return render(request, "partials/_product-modal.html", {"product": product})
