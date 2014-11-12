# -*- coding: utf-8 -*-
'''
  Truncatable primes
  Problem 37
  
  The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

  Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

  NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
  
  Answer: 748317 Completed on Mon, 20 Oct 2014, 16:33

  https://projecteuler.net/problem=37
  
  @author Botu Sun
'''

# Cannot have even digits.
# First digit can be 2, 3, 5, 7
# Middle digits can be 3, 5, 7, 9
# Last digit can be 3, 5, 7

import math

map = {2: True, 1: False}

def IsPrime(n):
  global map
  if map.has_key(n):
    return map.get(n)
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      map[n] = False
      return False
  map[n] = True
  return True

def ValidNumberForRecursion(n):
  digits = len(str(n))
  b = n 
  while b != 0:
    if not IsPrime(b):
      return False
    b = b % int(math.pow(10, digits - 1))
    digits -= 1
  return True
  
def ValidNumberFromRight(n):
  while n != 0:
    if not IsPrime(n):
      return False
    n /= 10
  return True
    
def Recursion(n, digits):
  global sum
  if ValidNumberForRecursion(n):
    if ValidNumberFromRight(n):
      print n
      sum += n
    Recursion(n + 1 * int(math.pow(10, digits)), digits + 1)
    Recursion(n + 2 * int(math.pow(10, digits)), digits + 1)
    Recursion(n + 3 * int(math.pow(10, digits)), digits + 1)
    Recursion(n + 5 * int(math.pow(10, digits)), digits + 1)
    Recursion(n + 7 * int(math.pow(10, digits)), digits + 1)
    Recursion(n + 9 * int(math.pow(10, digits)), digits + 1)
    
sum = 0 - 2 - 3 - 5 - 7


Recursion(2, 1)
Recursion(3, 1)
Recursion(5, 1)
Recursion(7, 1)
    
print sum
