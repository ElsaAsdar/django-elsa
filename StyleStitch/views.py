
# blog/views.py

from django.shortcuts import render, get_object_or_404
from .models import Category, Page, Blog

def home(request):
    categories = Category.objects.all()
    pages = Page.objects.filter(is_published=True)
    posts = Blog.objects.filter(status=1)
    return render(request, 'home.html', {'categories': categories, 'pages': pages, 'posts': posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def contact(request):
    posts = Blog.objects.filter(status=1)
    return render(request, 'contact.html', {'posts': posts})

def product(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'product.html', {'pages': pages})

def blog(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'blog.html', {'pages': pages})

def product_dress(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'product_dress.html', {'pages': pages})

def product_blous(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'product_blous.html', {'pages': pages})

def product_kemeja(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'product_kemeja.html', {'pages': pages})



def about(request):
    pages = Page.objects.filter(is_published=True)
    return render(request, 'about.html', {'pages': pages})
