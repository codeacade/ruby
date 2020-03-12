
# Pre-created class "Car":

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
    
  # New method that shows all "Car"'s properties in kind verbose mode.
  def display_car(self):
    return "This is a {} {} with {} MPG.".format(self.color, self.model, self.mpg)

# Creating instance of "Car" method and calling it's methods:
my_car = Car("DeLorean", "silver", 88)
print(my_car.display_car())
