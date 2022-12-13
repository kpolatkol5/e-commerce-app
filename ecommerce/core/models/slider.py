from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image


class Slider(models.Model):
    large_image = models.ImageField(verbose_name=_("Large Image"), upload_to=None , help_text=_("big picture for slider"))
    small_image = models.ImageField(verbose_name=_("Small Image"), upload_to=None , help_text=_("small picture for slider"))
    shape = models.ImageField(verbose_name=_("Shape") , upload_to=None , help_text=_("sliding figure behind the slider"))
    title = models.CharField(verbose_name=_("Title") , max_length=20)
    colorful_hood = models.CharField(_("Color hood"), max_length=20)
    color_of_the_title = models.CharField(verbose_name=_("color of the title"), default="#606da6" ,max_length=20)
    slogan = models.CharField(verbose_name=_("Slogan"), max_length=20)
    tagline = models.CharField(verbose_name=_("Tagline"), max_length=50 ,help_text=_("a slogan on the slider") )
    description2 = models.CharField(max_length=40 , verbose_name=_("Descripton 2"))
    slider_background_color = models.CharField(max_length=10 , verbose_name=_("slider background color") , default="#f0f5f9")
    def __str__(self):
        return self.title


    def save(self, *agrs, **kwargs):
        super().save(*agrs, **kwargs)
        if self.large_image:
            img = Image.open(self.large_image.path)
            if img.height > 468 or img.width >  992:
                output_size = (468,  992)
                img.thumbnail(output_size)
                img.save(self.large_image.path)

        if self.small_image:
            img = Image.open(self.small_image.path)
            if img.height > 289  or img.width > 456:
                output_size = (289, 456)
                img.thumbnail(output_size)
                img.save(self.small_image.path)