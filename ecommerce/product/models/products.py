from django.utils.text import slugify
from django.db import models
from product.models.categories import Categories
from product.models.tags import Tags
# from product.models.comments import Comments
from datetime import datetime


PRODUCT_TYPE = (
    ('Fiziksel ürün', 'P'),
    ('Dijital Ürün', 'D')
)


class Products(models.Model):

    name = models.CharField(max_length=255, verbose_name="Ürün Adı")
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    # it will change to CKeditor
    description = models.TextField(verbose_name="Ürün Açıklaması")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Satış Fiyatı")
    stock = models.IntegerField(verbose_name='Stok Sayısı')
    sku_code = models.CharField(max_length=30 , unique=True , null=True)
    category = models.ForeignKey(Categories, related_name="products", on_delete=models.CASCADE)
    product_type = models.CharField(choices=PRODUCT_TYPE, max_length=20, verbose_name="Ürün Tipi" ,help_text="P fiziksel D djital ürünü temsil eder")
    tags = models.ManyToManyField(Tags, verbose_name="Etiketler", related_name="products")
    barcode = models.CharField(max_length=50, verbose_name="Ürün Barkodu")
    is_active = models.BooleanField(default=True, verbose_name="Durumu")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')
    is_variations = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.name}"

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Products.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"
    # returns product's rate
    def get_total_rate(self):
        comments = Comments.objects.filter(product__id=self.id, is_active=True)
        rate_average = 0
        for comment in comments:
            rate_average += comment.get_like_count()

        return rate_average / 5

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = self.get_unique_slug()

        return super(Products, self).save(*args, **kwargs)


class Product_Image(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name="product_image",
        verbose_name="Ürün",
    )
    image = models.ImageField(
        upload_to=f"{datetime.now().year}/{datetime.now().month}/Product"
    )

    def __str__(self):
        return f"{self.product.name}"

    class Meta:
        verbose_name = "Ürünler Resimi"
        verbose_name_plural = "Ürünler Resimleri"
