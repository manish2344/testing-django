# views.py
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.with_category().all()
    return render(request, 'product_list.html', {'products': products})
