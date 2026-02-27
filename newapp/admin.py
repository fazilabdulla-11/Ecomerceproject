from django.contrib import admin

from newapp.models import Category, Product

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)