from django.shortcuts import render
from .models import Category, Customer, Product, Order

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'products': product})

def about(request):
    return render(request, 'about.html', {})
