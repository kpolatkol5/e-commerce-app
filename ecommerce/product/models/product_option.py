from django.db import models
from product.models.products import Products


class Option(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="orpsiyon adi "
    )
    is_active = models.BooleanField(default=True , verbose_name="Aktif Mi")
    def __str__(self):
        return self.name


class Option_value(models.Model):
    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE,
        verbose_name="Option", null=True ,
        related_name="optiyon_value",
    )

    name = models.CharField(
        max_length=50,
        verbose_name="opsiyon adi"
    )

    is_active = models.BooleanField(default=True , verbose_name="Aktif Mi")
    def __str__(self):
        return self.name


class Product_variations(models.Model):
    product = models.ForeignKey(
        Products,
        verbose_name="urun seçin",
        on_delete=models.CASCADE
    )

    option_value = models.ForeignKey(
        Option,
        verbose_name=" Opsiyon",
        on_delete=models.CASCADE,
        null=True
    )
    # option = models.ForeignKey(Option_value, verbose_name="Opsiyon Değeri", on_delete=models.CASCADE , null=True )

    def __str__(self):
        return f"{self.option_value} ==>  {self.product}"


class Sku(models.Model):
    sku = models.CharField(
        max_length=50,
        verbose_name="SKU Code"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Satış Fiyatı"
    )

    stock = models.IntegerField(
        verbose_name='Stok Sayısı'
    )

    def __str__(self):
        return f" ==>  {self.sku}"


class Product_variation_options(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="Ürün"
    )

    product_variations_id = models.ManyToManyField(
        Option_value,
        verbose_name="Ürün Varyasyonu seçiniz",
        related_name="tum_varyasyon"
    )

    sku_id = models.ForeignKey(
        Sku,
        verbose_name="Sku Seçin",
        on_delete=models.CASCADE,
        unique=True
    )

    name = models.CharField(
        max_length=50,
        verbose_name="Ürün için varyasyon ismi "
    )

    def __str__(self):
        return f"{self.product} ürününün | {self.sku_id.sku} stok koduna sahip | {self.name} varyasyonu"
