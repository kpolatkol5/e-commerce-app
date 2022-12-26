from product.models.categories import Categories


def custom_context_processors(request):
    context = {
        'categori': Categories.objects.all(),

    }

    return context
