from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.
def cart_summery(request):
    return render(request, 'cart_summery.html', {})

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    # test for post
    if request.POST.get('action') == 'post':
        
         # Get stuff
         product_id = int(request.POST.get('product_id'))
         product_qty = int(request.POST.get('product_qty'))
        
         # lookup product in the databse
         product = get_object_or_404(Product, id=product_id)

         # save to session
         cart.add(product=product, quantity=product_qty)

         # Get cart quantity
         cart_quantity = cart.__len__()

         # Return response
         # response  =JsonResponse({'Product Name:': product.name})
         response  =JsonResponse({'qty': cart_quantity})
         return response

def cart_delete(request):
    pass

def cart_update(request):
    pass