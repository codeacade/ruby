# this is ready-to-go example from codeacademy
# link: 
# https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes/exercises/its-not-all-animals-and-fruits
#
# but still there is something to do:
#
# Create an instance of ShoppingCart called my_cart. 
# Initialize it with any values you like,
# then use the add_item method to add an item to your cart.


class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print(product + " added.")
    else:
      print(product + " is already in the cart.")

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print(product + " removed.")
    else:
      print(product + " is not in the cart.")
  def list_items(self):
    """List all products from cart."""
    count_items=0
    for i in self.items_in_cart:
      count_items+=1
      print("Item ID:{}, item name: {}, item price {}.".format(str(count_items),i,self.items_in_cart[i]))

# end
