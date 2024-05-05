# blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('blog/<slug:slug>/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    
]

