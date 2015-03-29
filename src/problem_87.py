# -*- coding: utf-8 -*-
'''
  Prime power triples
  Problem 87
  
  The smallest number expressible as the sum of a prime square, prime cube, and 
  prime fourth power is 28. In fact, there are exactly four numbers below fifty 
  that can be expressed in such a way:
  
  28 = 2^2 + 2^3 + 2^4
  33 = 3^2 + 2^3 + 2^4
  49 = 5^2 + 2^3 + 2^4
  47 = 2^2 + 3^3 + 2^4
  
  How many numbers below fifty million can be expressed as the sum of a prime 
  square, prime cube, and prime fourth power?

  Answer: 1097343 Completed on Mon, 30 Mar 2015, 01:23
  https://projecteuler.net/problem=87
  
  @author Botu Sun
'''
from lib import math_utils

primes = math_utils.get_prime_list(10000)

limit = 50000000
numbers = {}

for p1 in primes:
  for p2 in primes:
    if p2 ** 3 + p1 ** 2 > limit:
      break
    for p3 in primes:
      if p3 ** 4 + p2 ** 3 + p1 ** 2 > limit:
        break
      numbers[p3 ** 4 + p2 ** 3 + p1 ** 2] = True

print len(numbers)