# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/iseven
#
# Define a function is_even that will take a number x as input.
# If x is even, then return True.
# Otherwise, return False.

def is_even(x):
    if x %2 == 0:
        return True
    return False
print is_even(900)

# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/isint
#
# Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer (as defined above) and False otherwise.

def is_int(x):
  return (x%1==0)

# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/digitsum
#
# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number’s digits. 
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. 
# (Assume that the number you are given will always be positive.)

def digit_sum(n):
  result=0
  for i in str(n):
    result+=int(i)
  return result

# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/factorial
#
# Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.

def factorial(x):
  result=1
  for i in range(1,x+1):
    result*=i
  return result

#
#
#


