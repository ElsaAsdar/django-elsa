# blog/urls.py

from django.urls import path
from . import views

app_name = 'StyleStitch'

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.category_list, name='category_list'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('blog/', views.blog, name='blog'),
    path('product_dress/', views.product_dress, name='product_dress'),
    path('product_blous/', views.product_blous, name='product_blous'),
     path('product_kemeja/', views.product_kemeja, name='product_kemeja'),
    path('about/', views.about, name='about'),
    
]

