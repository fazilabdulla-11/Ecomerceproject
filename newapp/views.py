from django.shortcuts import render,redirect

from newapp.models import Product

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    data=Product.objects.all().order_by('-created_at')[:4]
    return render(request,'index.html', {'products': data})

def all_products(request):
    data=Product.objects.all().order_by('-created_at')
    return render(request,'all_products.html', {'products': data})  

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html', {'error': 'Invalid username or password'})
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        confirm_password = request.POST.get('confirmpassword')
        if password != confirm_password:
            return render(request,'register.html', {'error': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            return render(request,'register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request,'register.html', {'error': 'Email already exists'})
        user=User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        return redirect('/login/')
        
            
    return render(request,'register.html')



def sign_out(request):
    logout(request)
    return redirect('home')