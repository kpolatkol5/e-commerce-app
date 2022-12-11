from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    role_name = models.CharField(max_length=50 , verbose_name=_("Role Name"))
    role_active = models.BooleanField(verbose_name = _("The role is active"))

    def __str__(self):
        return self.role_name
        
