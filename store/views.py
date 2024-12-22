from django.shortcuts import render
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def Home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products":products})


def About(request):
    return render(request, 'about.html')

def Login_User(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, "You have successfully logged in")
    #         return redirect('home')
    #     else:
    #         messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

def Logout_User(request):
    pass