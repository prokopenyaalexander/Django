from .views import BlogListView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),

]