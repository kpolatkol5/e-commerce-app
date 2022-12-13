from django.db import models
from django.utils.text import slugify


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
