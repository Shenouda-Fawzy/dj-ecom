from django.db import models
from datetime import datetime

# Create your models here.

# Category
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

# Customer
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


# Product
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7) # This is 7 digits (including decimal point) 99999.99
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # on_delete=CASCADE will delete the product if its category got deleted
    description = models.CharField(max_length=200, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product')

# Hello from the backend
    def __str__(self) -> str:
        return self.name

# Order
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address= models.CharField(max_length=200, blank=True, default='')
    phone_number= models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.today)
    status= models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.product}'