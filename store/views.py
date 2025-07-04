from django.shortcuts import render, redirect
from .models import Category, Customer, Product, Order
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'products': product})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have being logged in!"))
            return redirect('home')
        else:
            messages.error(request, ("There was an error logging you in. Please try again."))
            return redirect(request, 'login')
    
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully...Thanks!")
    return redirect('home')
