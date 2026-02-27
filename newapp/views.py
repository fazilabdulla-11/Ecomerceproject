from django.shortcuts import render

from newapp.models import Product

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_products(request):
    data=Product.objects.all()
    return render(request,'all_products.html', {'products': data})    