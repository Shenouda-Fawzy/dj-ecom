from django.contrib import admin
from .models import Order, Customer, Category, Product

# Register your models here.
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)