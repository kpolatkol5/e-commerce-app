from django.utils.text import slugify
from django.db import models
from product.models.categories import Categories
from product.models.tags import Tags

PRODUCT_TYPE = (
    ('P', 'Fiziksel ürün'),
    ('D', 'Dijital Ürün')
)


class Products(models.Model):
    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

    name = models.CharField(max_length=255, verbose_name="Ürün Adı")
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
    # it will change to CKeditor
    description = models.TextField(verbose_name="Ürün Açıklaması")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Satış Fiyatı")
    stock = models.IntegerField(verbose_name='Stok Sayısı')
    category = models.ForeignKey(
        Categories,
        related_name="products",
        on_delete=models.CASCADE
    )
    product_type = models.CharField(
        choices=PRODUCT_TYPE, max_length=1, verbose_name="Ürün Tipi")
    tags = models.ManyToManyField(
        Tags, verbose_name="Etiketler")
    barcode = models.CharField(max_length=50, verbose_name="Ürün Barkodu")
    is_active = models.BooleanField(default=True, verbose_name="Durumu")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Güncellenme Tarihi')

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
