# -*- coding: utf-8 -*-
'''
  Totient permutation
  Problem 70
  
  Euler's Totient function, φ(n) [sometimes called the phi function], is used to
  determine the number of positive numbers less than or equal to n which are 
  relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than
  nine and relatively prime to nine, φ(9)=6.
  The number 1 is considered to be relatively prime to every positive number, so
  φ(1)=1.

  Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation 
  of 79180.

  Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the
  ratio n/φ(n) produces a minimum.

  Answer: 8319823 Completed on Wed, 3 Dec 2014, 10:08
  https://projecteuler.net/problem=70
  
  Looking at the forum, there're plenty of better solutions if we use trick in 
  math: primes are impossible, n and n-1 couldn't be permunations. Then try two
  primes, if their multiplication is under the limit and of same permunation, we
  will find our answer. The answer with 2 primes will always be better than that
  with 3 primes so no need to continue.
  I'll keep my brute-force here anyway.
  
  @author Botu Sun
'''

import math
import sys
from lib import math_utils

LIMIT = 10000000

prime_checker = math_utils.PrimeFactorsGenerator(LIMIT)
primes = prime_checker.get_prime_list()
prime_factors = prime_checker.get_prime_factors()
print 'Primes generated'

min_ratio = sys.maxint
min_n = 0

for i in xrange(2, LIMIT + 1):
  # If the number has a factor < 100, the ratio would be very big.
  if prime_factors[i][0] < 100: 
    continue
  phi = math_utils.totient(i, prime_factors[i])
  if sorted(str(phi)) != sorted(str(i)):
    continue
  ratio = i / float(phi)
  if ratio < min_ratio:
    min_ratio = ratio
    min_n = i

print min_ratio, min_n
