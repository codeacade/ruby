# All new world of lambdas, the Anonymous Functions...
# https://www.codecademy.com/courses/learn-python/lessons/advanced-topics-in-python/exercises/anonymous-functions

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# Fill in the first part of the filter function with a lambda. 
# The lambda should ensure that only "Python" is returned by the filter.

languages = ["HTML", "JavaScript", "Python", "Ruby"]   # -given
print(filter(lambda x:x == "Python", languages))


# Create a list, squares, that consists of the squares of the numbers 1 to 10. 
# A list comprehension could be useful here!
# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).

sqlist = [i*i for i in range(1,11)]
print(filter(lambda x: x>30 and x<70,sqlist))

