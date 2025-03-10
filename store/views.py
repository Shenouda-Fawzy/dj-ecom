from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .forms import SignupForm


def Home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {"products": products})


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
    flash_success(request, "You have successfully logged out")
    return redirect('store:home')


def Register_User(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            
            # Save creates and saves a database object from the data bound to the form
            form.save()
            
            # Authenticating and login the user
            username = form.cleaned_data["user_name"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)

            flash_success(request, "You've registered successfully!")
            return redirect("store:home")
    else:
        flash_success(request, "Whoops there was a problem registering!! please try again")
        return render(request, "register.html")


def flash_error(request, msg):
    messages.error(request, msg, extra_tags="alert alert-danger")


def flash_success(request, msg):
    messages.success(request, msg, extra_tags="alert alert-success")