from django.contrib import admin
from product.models.categories import Categories
from product.models.products import Products
from product.models.comments import Comments
from product.models.tags import Tags

admin.site.register(Categories)
admin.site.register(Comments)
admin.site.register(Products)
admin.site.register(Tags)
