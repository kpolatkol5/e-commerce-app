from django.db import models
from django.utils.text import slugify
from mptt.models import TreeForeignKey, MPTTModel


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

    def get_parent_tree(self):
        return self.get_ancestors(ascending=False, include_self=True)

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
