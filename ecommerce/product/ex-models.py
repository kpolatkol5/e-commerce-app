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
