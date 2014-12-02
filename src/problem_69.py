# -*- coding: utf-8 -*-
'''
  Totient maximum
  Problem 69
  Euler's Totient function, φ(n) [sometimes called the phi function], is used to
  determine the number of numbers less than n which are relatively prime to n. 
  For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively 
  prime to nine, φ(9)=6.
  
  n	Relatively Prime	φ(n)	n/φ(n)
  2	1	1	2
  3	1,2	2	1.5
  4	1,3	2	2
  5	1,2,3,4	4	1.25
  6	1,5	2	3
  7	1,2,3,4,5,6	6	1.1666...
  8	1,3,5,7	4	2
  9	1,2,4,5,7,8	6	1.5
  10	1,3,7,9	4	2.5
  It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

  Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

  Answer: 510510 Completed on Tue, 2 Dec 2014, 16:33
  https://projecteuler.net/problem=69
  
  @author Botu Sun
'''

import math
from lib import math_utils

LIMIT = 1000000

prime_checker = math_utils.PrimeFactorsGenerator(LIMIT)
primes = prime_checker.get_prime_list()
prime_factors = prime_checker.get_prime_factors()
print 'Primes generated'

max_ratio = 0
max_n = 0

for i in xrange(2, LIMIT + 1):
  phi = math_utils.totient(i, prime_factors[i])
  ratio = i / float(phi)
  if ratio > max_ratio:
    max_ratio = ratio
    max_n = i

print max_n, max_ratio