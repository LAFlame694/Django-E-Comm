from .cart import Cart

# Create context processors so our cart can work on all pages of our site.
def cart(request):
    # Return the default data from our cart
    return {'cart': Cart(request)}