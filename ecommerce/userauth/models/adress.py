from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    if value is "Null":
        return value
    else:
        print(value)

        if str(value).startswith("5"):
            if len(str(value)) == 10:
                return value
            else:
               raise ValidationError(_("phone numbers must be 10 digits"))
        else:
            raise ValidationError(_("Phone Numbers should start with 05"))


class Adress(models.Model):
    first_name = models.CharField(max_length=20 , verbose_name=_("Name"))
    last_name = models.CharField(max_length=25 , verbose_name=_("Surname"))
    phone_number = models.IntegerField(verbose_name=_("Mobile Phone") , unique=True , validators = [validate_phone_number])
    email_adress = models.EmailField(max_length = 254 , verbose_name=_("Email Adress"))
    is_active = models.BooleanField(verbose_name=_("Active User"))
    city = models.CharField(max_length=30 , verbose_name = "City")
    town = models.CharField(max_length=30 , verbose_name = "Town")
    country = models.CharField(max_length=30 , verbose_name=_("Country"))
    mailing_address = models.TextField(verbose_name=_("Mailing Address"))


    def __str__(self):
        return self.first_name + self.last_name + " ==> "+ self.email_adress 


class BillingAdress(models.Model):
    registered_addresses = models.ForeignKey(Adress , verbose_name=_("Registered Addresses") , help_text=_("you don't have to choose (optional)") , null=True , blank=True , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20 , verbose_name=_("Name"),null=True , blank=True )
    last_name = models.CharField(max_length=25 , verbose_name=_("Surname"),null=True , blank=True )
    phone_number = models.IntegerField(verbose_name=_("Mobile Phone") , unique=True , validators = [validate_phone_number],null=True , blank=True )
    email_adress = models.EmailField(max_length = 254 , verbose_name=_("Email Adress"),null=True , blank=True )
    is_active = models.BooleanField(verbose_name=_("Active User"),null=True , blank=True )
    city = models.CharField(max_length=30 , verbose_name = "City",null=True , blank=True )
    town = models.CharField(max_length=30 , verbose_name = "Town",null=True , blank=True )
    country = models.CharField(max_length=30 , verbose_name=_("Country"),null=True , blank=True )
    mailing_address = models.TextField(verbose_name=_("Mailing Address"),null=True , blank=True )

    def save(self , *args, **kwargs):
        if self.registered_addresses is not None:
            self.first_name = None
            self.last_name = None
            self.phone_number = None 
            self.email_adress  = None
            self.is_active = None
            self.city = None
            self.town = None
            self.country =  None
            self.mailing_address = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.first_name + self.last_name + " ==> "+ self.email_adress 
