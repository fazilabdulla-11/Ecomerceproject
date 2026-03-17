from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    

    name = models.CharField(max_length=255)
    image =models.ImageField(upload_to='product/', default='products/default.jpg')
    brand = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    size = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
        
class Cart(models.Model):
    cartid= models.CharField(max_length=100)

        
class Cartitem(models.Model):
    CART=models.ForeignKey(Cart,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    cteated_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    




