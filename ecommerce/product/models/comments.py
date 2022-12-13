from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from userauth.models import Kullanicilar
from product.models.products import Products


class Comments(models.Model):
    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
    user = models.ForeignKey(
        Kullanicilar, on_delete=models.CASCADE, verbose_name='Müşteri')
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name="Ürün")
    comment = models.TextField(verbose_name='Yorum')
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name="Yıldız")
    is_active = models.BooleanField(default=True, verbose_name="Durumu")

    def __str__(self):
        return f"{self.comment[:15]}... => {self.rating} Puan"

    def get_like_count(self):
        return self.rating
