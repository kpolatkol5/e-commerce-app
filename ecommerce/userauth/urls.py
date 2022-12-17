from django.urls import path
from userauth.views.aut_view import login_view,register_view,logout_view
from django.contrib.auth import views as auth_views 


urlpatterns = [
    path('login/',login_view , name="login"),
    path('register/',register_view , name="register"),
    path('logout',logout_view , name="logout"),




]
