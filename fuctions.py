
"""
#say hello world

def say_hello():
  print("Hello,World!")

say_hello()

=======
#sum of 2 nums

def add(a,b):
  return a+b
  
result = add(1098,865)
print(result)

=======
"""
#greeting with name
'''
def greet(name):
  print("hello", name)
  

greet("indira")



def check_even_odd(n):
  if n%2 == 0:
    return "Even"
  else:
    return "Odd"

print(check_even_odd(710))'''

#square of num
"""
def find_square(n):
  return n*n

print(find_square(2))"""

#largest of 2 num
"""
def Find_largest(a,b):
  if a < b:
    return b
  else:
    return a
  
print(Find_largest(10,100))"""

#lagerest of 3

"""
def fid_largest_of_3(a,b,c):
  if a >= b and a >= c:
    return a
  elif b >= a and b >=c:
    return b
  
  elif c >= a and c >=b:
    return c
  
print(fid_largest_of_3(2,100,29))

"""

#len of string
"""
def str_len(string):
  count = 0
  for _ in string:
    count += 1
  return count

print(str_len("paki  stan"))

"""

# prime number
"""
def is_prime(n):
  if n <= 1:
    return False
  
  for i in range(2,n):
    if n% i == 0:
      return False
  return True


print(is_prime(111))
"""
# leap year
"""
def is_leap(num):
  if ( num % 4 == 0 and num % 100 != 0 ) or (num % 400 == 0):
    return True
  return False

print(is_leap(2000))"""


# factorial

"""
def factorial(n):
  result = 1
  for i in range(1,n+1):
    result *=i
  return result

print(factorial(3))
"""
#sum from one to n
"""
def sum_of_numbers(n):
  total = 0

  for i in range(1 , n+1):
    total += i

  return total


print(sum_of_numbers(10))"""

#count vowels

def count_vowels(str):
  count = 0
  vowels = "aeiouAEIOU"

  for char in str:
    if char in vowels:
      count += 1
      
  return count
  
print(count_vowels("Hello world"))