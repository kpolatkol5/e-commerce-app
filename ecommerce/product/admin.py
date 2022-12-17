from django.contrib import admin
from product.models.categories import Categories
from product.models.products import Products
from product.models.comments import Comments
from product.models.tags import Tags
from product.models.product_option import *
from mptt.admin import DraggableMPTTAdmin

admin.site.register(Categories , DraggableMPTTAdmin)
admin.site.register(Comments)
admin.site.register(Products)
admin.site.register(Tags)

admin.site.register(Option)
admin.site.register(Product_variations)
admin.site.register(Sku)
admin.site.register(Product_variation_options)
admin.site.register(Option_value)

