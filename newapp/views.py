from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def all_products(request):
    return render(request,'all_products.html')    