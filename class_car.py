
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
  # New method that sets "condition" variable i cars was used.
  def drive_car(self):
    self.condition = "used"
    
    
# Creating instance of "Car" method and calling it's methods:
my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
