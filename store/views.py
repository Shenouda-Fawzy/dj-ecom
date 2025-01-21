from django.shortcuts import redirect, render
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
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            flash_success(request, "You have successfully logged in")
            return redirect('store:home')
        else:
            flash_error(request, "Invalid username or password")
            return redirect('store:home')
    else:
        return render(request, 'login.html')

def Logout_User(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('store:home')

def flash_error(request, msg):
    messages.error(request, msg, extra_tags="alert alert-danger")

def flash_success(request, msg):
    messages.success(request, msg, extra_tags="alert alert-success")