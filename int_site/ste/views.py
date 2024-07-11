from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.
def home(request):
    prod = Product.objects.all()
    return render(request, "index.html",{
        'prod': prod
    })
def view_product(request, id):
    products = Product.objects.filter(id=id).first()
    print(products)
    return render(request, 'products.html',{'products':
    products
    })