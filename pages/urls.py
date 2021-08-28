from django.urls import path
from . import views

urlpatterns = [
    #path('', views.homePageView, name='home'),
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view() , name='about'),
]