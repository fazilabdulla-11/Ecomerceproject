from django.shortcuts import render,redirect

from newapp.models import Product,Cart,Cartitem,Adress,Order

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.

def index(request):
    data=Product.objects.all().order_by('-created_at')[:4]
    return render(request,'index.html', {'products': data})

def all_products(request):
    

    data=Product.objects.all().order_by('-created_at')
    qry = request.GET.get('q')

    if qry:
        data=Product.objects.filter(Q(name__icontains=qry)|Q(description__icontains=qry)).order_by('-created_at')

    paginator = Paginator(data, 5)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    data1 = paginator.get_page(page_number)
    return render(request,'all_products.html', {'page_obj': data1})  

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

def product_details(request,id):
    data=Product.objects.get(id=id)                          
    
    return render(request,'product_details.html',{'p':data})    



def womens_details(request):
    data=Product.objects.filter(Q(gender__contains="F")|Q(gender__contains="U")).order_by('-created_at')

    return render(request,'womens_details.html',{'p':data})


def cartid(request):
    cid=request.session.session_key
    if not cid:
        request.session.create()
        cid=request.session.session_key
    return cid

def add_to_cart(request, p_id):
    product=Product.objects.get(id=p_id)
    c_id=cartid(request)
    try:
        cart =Cart.objects.get(cartid=c_id)
    
    except:
        cart=Cart.objects.create(cartid=c_id)
        cart.save()

    try:
        cart_item=Cartitem.objects.filter(CART=cart,PRODUCT=product).first()
    
        cart_item.quantity += 1
        cart_item.save()
    except:
        cart_item=Cartitem.objects.create(CART=cart,PRODUCT=product,quantity=1)
        cart_item.save()
    

    return redirect('cart_details')

def minimize_from_cart(request,p_id):
    product=Product.objects.get(id=p_id)
    c_id=cartid(request)
    cart =Cart.objects.get(cartid=c_id)
    
    cart_item=Cartitem.objects.filter(CART=cart,PRODUCT=product).first()
    if cart_item.quantity == 1:
        cart_item.delete()

    else:
        cart_item.quantity -= 1
        cart_item.save()  



    return redirect('cart_details')       


    

def cart_details(request):
    cart_items = Cartitem.objects.filter(CART__cartid=cartid(request))
    return render(request,'cart_details.html', {'cart_items': cart_items})

    
def remove_cart_item(request,p_id):
    product=Product.objects.get(id=p_id)
    cid = cartid(request)
    cart = Cart.objects.get(cartid=cid)
    cartitem = Cartitem.objects.filter(CART=cart, PRODUCT=product).first()
    if cartitem:
        cartitem.delete()



    return redirect('cart_details')



def buy_item(request, p_id):

    if request.method == 'POST':
        name = request.POST.get('name')
        district = request.POST.get('district')
        place = request.POST.get('place')
        post = request.POST.get('post')
        house = request.POST.get('house')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        user = request.user
        if not user.is_authenticated:
            return redirect('/login/')
        # address = Adress.objects.create(USER = user,name = name,place=place,post=post house=house, )


    return render(request,'buy.html')