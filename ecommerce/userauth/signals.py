from userauth.models.user_model import Kullanicilar
from userauth.models.profile import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Kullanicilar)
def create_profil(sender, instance, created, **kwargs):
    
    print(instance.username, "__Created: ", created) # Yeni profil olustugunda bool cikti alacagiz

    if created:
        UserProfile.objects.create(user=instance)