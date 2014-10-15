# -*- coding: utf-8 -*-
'''
  Pandigital products
  Problem 32
  
  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

  The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

  Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

  HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
  
  Answer: 45228 Completed on Wed, 15 Oct 2014, 23:07
  https://projecteuler.net/problem=32
  
  @author Botu Sun
'''

import math

def TestPandigital(s):
  if len(s) != 9 or '0' in s:
    return False
  map = {}
  for c in s:
    if map.has_key(c):
      return False
    map[c] = True
  return True
  
sum = 0
# The production can only fall in [1234, 9876]
for i in xrange(1234, 9877):
  for j in xrange(1, int(math.sqrt(i)) + 1):
    if i % j == 0:
      if TestPandigital(str(i) + str(j) + str(i / j)):
        sum += i
        break
        
print sum