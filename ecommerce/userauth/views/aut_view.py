from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate , login ,logout
from userauth.models.user_model import Kullanicilar 
from userauth.models.profile import UserProfile


from django.core.mail import EmailMessage
from django.contrib import messages
from django.urls import reverse
from time import sleep

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(request)
        user = authenticate(email=email,password=password)
        if user:
            if user.is_active:
                login(request,user)       
                return redirect(reverse('home-page'))
        else:
            messages.error(request,'E-posta veya şifre hatalı')
            return redirect(reverse('login'))
        
                
    return render(request,'userauth/login.html',)




def register_view(request):
    if request.method == "POST":
        name= request.POST["name"]
        username= request.POST["username"]
        email= request.POST["email"]
        password= request.POST["password"]
        repassword= request.POST["repassword"]
        phone = request.POST["phone"]
        
        if phone.startswith("0"):
            print("0 ile başlar")
            phone=phone[1:]
            print(phone)

        if Kullanicilar.objects.filter(email=email).exists():
            messages.error(request,'bu email adresi ile katılı hesap var ')
            return redirect(reverse('register'))
        else:
            if Kullanicilar.objects.filter(username=username).exists():
                messages.error(request,'bu kullanıcı adı kullanılıyor ')
                return redirect(reverse('register'))
            else:
                if UserProfile.objects.filter(phone_number=phone).exists():
                    messages.error(request,'cep telefonu  kullanılıyor ')
                    return redirect(reverse('register'))
                else:
                    if password == repassword :
                        Kullanicilar.objects.create_user(email=email , username = username,password=password)
                        user_profile = UserProfile.objects.get(user=Kullanicilar.objects.get(email=email))
                        user_profile.first_name = name
                        user_profile.phone_number = int(phone)
                        user_profile.save()
                        messages.success(request,'Kullanıcı Oluşturuldu')
                        # return redirect(reverse('login'))

                    else:
                        messages.error(request,'Şifreler uyuşmuyor')
                        return redirect(reverse('register'))

    return render(request,'userauth/register.html',)

def logout_view(request):
    logout(request)
    return redirect(reverse("home-page"))