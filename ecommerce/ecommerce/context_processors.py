from product.models.categories import Categories


def custom_context_processors(request):
    context = {
        'categories': Categories.objects.all(),

    }

    return context
