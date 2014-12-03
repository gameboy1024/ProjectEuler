# -*- coding: utf-8 -*-
'''
  Ordered fractions
  Problem 71
  Consider the fraction, n/d, where n and d are positive integers. If n<d and 
  HCF(n,d)=1, it is called a reduced proper fraction.

  If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
  size, we get:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 
  5/7, 3/4, 4/5, 5/6, 6/7, 7/8

  It can be seen that 2/5 is the fraction immediately to the left of 3/7.

  By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending 
  order of size, find the numerator of the fraction immediately to the left of 
  3/7.

  Answer: 428570 Completed on Wed, 3 Dec 2014, 14:04
  https://projecteuler.net/problem=71
  
  @author Botu Sun
'''

import math
import sys
from lib import math_utils

LIMIT = 1000000

prime_checker = math_utils.PrimeFactorsGenerator(LIMIT)
primes = prime_checker.get_prime_list()
prime_factors = prime_checker.get_prime_factors()
print 'Primes generated'

target = 3.0 / 7

closest_f = 0.0
closest_n = 0
closest_d = 0

for i in xrange(8, LIMIT + 1):
  for j in xrange(int(closest_f * i), int(math.ceil(target * i))):
    f = float(j) / i
    if f > closest_f:
      closest_f = f
      closest_n = j
      closest_d = i

print closest_f, closest_d, closest_n
