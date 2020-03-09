# this is ready-to-go example from codeacademy
# link: 
# https://www.codecademy.com/courses/learn-python/lessons/introduction-to-classes/exercises/its-not-all-animals-and-fruits
#
# but still there is something to do:
#
# Create an instance of ShoppingCart called my_cart. 
# Initialize it with any values you like,
# then use the add_item method to add an item to your cart.


class ShoppingCart(object):         # SUPERCLASS (parent of other classes - see below)
  # (object) as class parameter means that it is inhering from "object" class, parent of all classes.
  # trimple quotes below are single-line-comment indicator (but bettter use ###) 
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):  # init paramaters will be required while crerating instance of the class (object)
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):  # this will be called by: object.add_item(product, price)
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
      
  def list_items(self):   # no standard parameters for this method, just "self" as for any method
    """List all products from cart."""
    count_items=0
    for i in self.items_in_cart:
      count_items+=1
      print("Item ID:{}, item name: {}, item price {}.".format(str(count_items),i,self.items_in_cart[i]))

# ########### inheritance exercise:  ################

class StaffCart(ShoppingCart):  # this extends class ShoppingCart()
  # if no __init__ method in child class, superclass (parent) ShoppingCart()'s __init__ in use!
  def newPrice(self, product, nPrice):
    if product in self.items_in_cart:
        self.items_in_cart[product] = nPrice
        print("New " + product + " price is " + str(nPrice))

    else:
        print(product + " is not in the cart.")

class testCart(ShoppingCart):  # this extends class ShoppingCart()
  def __init__(self):     # this has its own __init__method, no need to comply with superclass
    self.items_in_cart = {}  # has to have it declared to use it in "add_item" and "list_items" below
  def add_test(self):
    self.add_item("test"+str(len(self.items_in_cart)), 0)
    self.list_items()

    
# Load this module by: import ShoppingCart (after ShoppingCart.py filename) 
# Create instace (object) of its classes - use: ShoppingCart.testCart() - no need for parameter but must have()

eva = ShoppingCart.ShoppingCart("Eva")  # an instance (object) of super-class ShoppingCart()
print eva.items_in_cart   # first internal parameter of super-class ShoppingCart()
eva.add_item("banana", 12)  # first internal method (funcion) of super-class ShoppingCart()
eva.list_items()   # new added method (function) of super-class ShoppingCart()

steven = ShoppingCart.testCart()  # an instance (object) of child-class testCart()
steven.add_test()    # new added method (function) of of child-class testCart()

# end
