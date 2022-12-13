from django.urls import path 
from core.views.index import HomePageView
urlpatterns = [
    path("" ,HomePageView.as_view() , name="home-page" )
]
