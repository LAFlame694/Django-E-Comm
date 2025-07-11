from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists.
        cart = self.session.get('session_key')

        # If no cart exists, create a new empty cart in the session.
        # if the user is new, no session key! Create one.
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Make sure cart is available on all pages of site.
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        # If the product is already in the cart, don’t do anything
        if product_id in self.cart:
           pass
        else:
            # If it’s not in the cart, add it.
            self.cart[product_id] = int(product_qty)

        # Mark the session as changed so Django saves it.
        self.session.modified = True
    
    def cart_total(self):
        # get product IDs
        product_ids = self.cart.keys()

        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)

        # get quantities
        quantities = self.cart

        # start counting at 0
        total = 0
        for key, value in quantities.items():

            # convert key string into int so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)
                    
        
        return total
    
    # Returns the number of items in the cart.
    def __len__(self):

        # returns 3 if there are 3 products in the cart
        return len(self.cart)
    
    def get_prods(self):

        # Get ids from cart
        product_ids = self.cart.keys()

        # Use Ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)

        # return lookedup products
        return products

    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        # get cart
        ourcart = self.cart

        # update dictionary/ cart
        ourcart[product_id] = product_qty

        self.session.modified = True
        
        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        
        # delete from dictionary/ cart
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True