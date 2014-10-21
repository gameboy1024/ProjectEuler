# -*- coding: utf-8 -*-
'''
  Goldbach's other conjecture
  Problem 46
  
  It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

  9 = 7 + 2×12
  15 = 7 + 2×22
  21 = 3 + 2×32
  25 = 7 + 2×32
  27 = 19 + 2×22
  33 = 31 + 2×12

  It turns out that the conjecture was false.

  What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

  Answer: 5777 Completed on Tue, 21 Oct 2014, 23:06
  https://projecteuler.net/problem=46
  
  @author Botu Sun
'''

import math

map = {2: True, 3: True, 5: True, 7: True}

def IsPrime(n):
  global map
  if map.has_key(n):
    return map.get(n)
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  map[n] = True
  return True

i = 9
while (True):
  if IsPrime(i):
    map[i] = True
  else:
    j = 1
    while ((i - 2 * j * j) > 1):
      if map.has_key(i - 2 * j * j):
        break
      j += 1
    if (i - 2 * j * j) <= 1:
      print i
      exit(0)
  i += 2