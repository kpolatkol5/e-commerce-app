from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

# it will move to site-settings's models.py
# class Currency(models.Model):
#     class Meta:
#         verbose_name = "Para Birimi"
#         verbose_name_plural = "Para Birimleri"

#     name = models.CharField(max_length=255, verbose_name="Para Birimi")
#     symbol = models.CharField(
#         max_length=3, verbose_name="Para Birimi Sembolu")

# it will move to site-settings's models.py
# class TransportationType(models.Model):
#     class Meta:
#         verbose_name = "Kargo Seçeneği"
#         verbose_name = "Kargo Seçenekleri"

#     name = models.CharField(max_length=255, verbose_name="Gönderim Tipi")
#     price = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Gönderim Fiyatı")
#     lowest_minimum_price = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Minimum Taban Fiyatı")
#     is_active = models.BooleanField(default=True, verbose_name="Durumu")
#     created_at = models.DateTimeField(
#         auto_now_add=True, verbose_name='Oluşturulma Tarihi')
#     updated_at = models.DateTimeField(
#         auto_now=True, verbose_name='Güncellenme Tarihi')

#     def __str__(self):
#         return f"{self.name} | {self.price}"


class Tags(models.Model):
    class Meta:
        verbose_name = "Etiket"
        verbose_name_plural = "Etiketler"

    name = models.CharField(max_length=255, unique=True,
                            verbose_name='Etiket Adı')
    slug = models.SlugField(unique=True, verbose_name='Slug', editable=False)
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
        while Tags.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = self.get_unique_slug()

        return super(Tags, self).save(*args, **kwargs)


PRODUCT_TYPE = (
    ('P', 'Fiziksel ürün'),
    ('D', 'Dijital Ürün')
)


class Categories(MPTTModel):
    unique_together = ('slug', 'parent',)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    name = models.CharField(max_length=200, verbose_name="Kategori Adı")
    slug = models.SlugField(unique=True, editable=False)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])

    def get_unique_slug(self):
        slug = slugify(self.name.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Categories.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{counter}'
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = self.get_unique_slug()

        return super(Categories, self).save(*args, **kwargs)


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
        'Categories',
        related_name="products",
        on_delete=models.CASCADE
    )
    product_type = models.CharField(
        choices=PRODUCT_TYPE, max_length=1, verbose_name="Ürün Tipi")
    tags = models.ManyToManyField(Tags, verbose_name="Etiketler")
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
            print(comment)
            rate_average += comment.get_like_count()

        return rate_average / 5

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.slug = self.get_unique_slug()

        return super(Products, self).save(*args, **kwargs)


class Comments(models.Model):
    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, verbose_name='Müşteri') This will change with Kullanicilar Model
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name="Ürün")
    comment = models.TextField(verbose_name='Yorum')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Yıldız")
    is_active = models.BooleanField(default=True, verbose_name="Durumu")
    # like = models.ManyToManyField(Kullanicilar)

    def __str__(self):
        return f"{self.comment[:15]}... => {self.rating} Puan"

    def get_like_count(self):
        return self.rating
