from django.contrib import admin
from product.models.categories import Categories
from product.models.products import Products
from product.models.comments import Comments
from product.models.tags import Tags
from product.models.variants import Options, OptionValues, ProductOptions, ProductVariants, VariantValues

admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Products)
admin.site.register(Tags)

admin.site.register(Options)
admin.site.register(OptionValues)
admin.site.register(ProductOptions)
admin.site.register(ProductVariants)
admin.site.register(VariantValues)
