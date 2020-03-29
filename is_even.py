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

# or simpe: 

def is_even(x):
    return x%2 ==0


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
  result = 0
  for i in str(n):
    result += int(i)
  return result

# version.1 (using >>lambda<< and >>reduce (REDUCE GOT REMOVED FROM PYTHON3) << function):

def digit_sum(n):
  return reduce(lambda x,y:int(x)+int(y),str(n))

# version.2 using side evaluation (a,b = b,a):

def digit_sum(n):
   result = 0
   while n>0:
     n, result = int(n/10), result + n%10
   return result

# version.3 SIMPLEST POSSIBLE !!

def digit_sum(n):
    return sum([int(i) for i in str(n)])


# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/factorial
#
# Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.

def factorial(x):
  result=1
  for i in range(1,x+1):
    result*=i
  return result

# version.1 (using >>lambda<< and >>reduce (REDUCE GOT REMOVED FROM PYTHON3) << function):

def factorial(x):
  return reduce(lambda x,y:x*y, range(1,x+1)

# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/isprime
#
# Define a function called is_prime that takes a number x as input.
# For each number n from 2 to x - 1, test if x is evenly divisible by n.
# If it is, return False.
# If none of them are, then return True.

def is_prime(x):
  if x>1:
    return all(x%i!=0 for i in range(2,x))
  return False


# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/reverse
# 
# Define a function called reverse that takes a string textand returns that string in reverse. 
# For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with this.

def reverse(text):
  result=""
  for i in range(len(text)-1,-1,-1):
    result+=text[i]
  return result
                
# v.1 bit simpler
                
def reverse(text):
  result=""
  for i in text:
    result = i + result
  return result


# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/antivowel
# 
# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
# For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. 
# Make sure to remove lowercase and uppercase vowels.

# version.1

def anti_vowel(text):
  for i in "aeiouAEIOU":
    text = text.replace(i,"")
  return text

# version.2 without using string.replace(old, new, count) /https://www.geeksforgeeks.org/python-string-replace/

def anti_vowel(text):
  result=""
  for i in text:
    if not i in "aeiouAEIOU":
      result+=i
  return result

# version.3 using "for-if" structure from part 9

def anti_vowel(text):
  result = "".join([i for i in text if i not in "aeiouAEIOU"])
  return result



# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/scrabblescore
# 
# Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
# Assume your input is only one word containing no spaces or punctuation.
# As mentioned, no need to worry about score multipliers!
# Your function should work even if the letters you get are uppercase, lowercase, or a mix.
# Assume that you’re only given non-empty strings.

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}  # score dictionary is given

def scrabble_score(word):
  result=0
  word = word.lower()
  for i in word:
    result+=score[i]
  return result



# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/censor-
# 
# Write a function called censor that takes two strings, text and word, as input. 
# It should return the text with the word you chose replaced with asterisks. For example:
#  censor("this hack is good hacker hack", "hack")
# should return: 
#  "this **** is good hacker ****"
# Assume your input strings won’t contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters in the censored word.

def censor(text, word):
  text = text.split()
  result = "".join(["*"*len(i) if i==word else i for i in text])  # <<<<<< THIS iS BRILLIANT AND I HAVE TO USE IT
  return result
# a = [x if ... else y for i in b]  <<<< this is abslutely fantastic construction
# I have no idea why it is not tought first lesson of Python everywhere ??



# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/purify
# 
# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result. 
# For example, purify([1,2,3]) should return [2].

def purify(numbers):
  result = []
  for i in numbers:
    if i%2==0:
      result.append(i)
  return result

# same as above but usinf "for-if" scheme:

def purify(numbers):
    result = [i for i in numbers if i%2==0]
    return result


# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/product
# 
# Define a function called product that takes a list of integers as input and returns the product of all of the elements in the list. 
# For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
# Your function should return an integer.

def product(numbers):
  result = 1
  for i in numbers:
    result*=i
  return result

###### SUPEREASY #######


# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/removeduplicates
# 
# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.

def remove_duplicates(numbers):
  result=[]
  for i in numbers:
    if not i in result:
      result.append(i)
  return result



# https://www.codecademy.com/courses/learn-python/lessons/practice-makes-perfect/exercises/median
# 
# Write a function called median that takes a list as an input and returns the median value of the list. 
# For example: median([1, 1, 2]) should return 1.
# The list can be of any size and the numbers are not guaranteed to be in any particular order. Make sure to sort it!
# If the list contains an even number of elements, your function should return the average of the middle two.

def median(n):
  n.sort()
  l = len(n)
  if l%2:
    return n[(l-1)/2]
  return (n[l/2]+n[l/2-1])/2.0

# END OF SECTION


