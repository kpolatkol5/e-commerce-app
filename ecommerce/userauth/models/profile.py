from django.db import models
from userauth.models.user_model import Kullanicilar
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from userauth.models.role import Role
from userauth.models.adress import Adress , BillingAdress

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

            
    
class UserProfile(models.Model):
    user = models.OneToOneField(Kullanicilar , verbose_name=_("Users") , on_delete = models.CASCADE)
    first_name = models.CharField(max_length=20 , verbose_name=_("Name"))
    last_name = models.CharField(max_length=25 , verbose_name=_("Surname"))
    phone_number = models.IntegerField(verbose_name=_("Mobile Phone") , unique=True , validators = [validate_phone_number] , null=True , blank=True)
    date_of_birth = models.DateField(verbose_name=_("Date Of Birth"), null=True , blank=True) 
    validate_user = models.BooleanField(default=False , verbose_name=_("Verified User"))
    is_active = models.BooleanField(verbose_name=_("Active User") ,default=False)
    address = models.ForeignKey( Adress , verbose_name=_("The address of the user") ,on_delete=models.CASCADE , null=True , blank=True)
    billing_address = models.ForeignKey(BillingAdress , verbose_name=_("User's billing address") , on_delete=models.CASCADE ,  null=True , blank=True)
    user_role = models.ForeignKey(Role , verbose_name=_("The Role Of The User") , on_delete = models.CASCADE ,  null=True , blank=True)


    def __str__(self):
        return f"{str(self.first_name) + str(self.last_name)} ==> {self.user.email}"
        

        