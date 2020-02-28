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


# Call the appropriate method on movies such that it will print out all the items (hint, hint) in the dictionary—that is,
# each key and each value.

movies = {
  "Monty Python and the Holy Grail": "Great",
  "Monty Python's Life of Brian": "Good",
  "Monty Python's Meaning of Life": "Okay"
}

print(movies.items())


# Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) 
# that are evenly divisible by 3 or 5.

threes_and_fives = [i from i in range(1,16) if i%3 or i%5]
print(threes_and_fives)


# The string in the editor is garbled in two ways:
# - Our message is backwards.
# - The letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print(message)


# Create a new variable called message.
# Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s. 
# The second argument will be garbled.
# Finally, print your message to the console.

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!="X", garbled)
print(message)

