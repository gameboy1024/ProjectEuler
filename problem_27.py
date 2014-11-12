# -*- coding: utf-8 -*-
'''
  Quadratic primes
  Problem 27
  
  Euler discovered the remarkable quadratic formula:

  n² + n + 41

  It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

  The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

  Considering quadratics of the form:

  n² + an + b, where |a| < 1000 and |b| < 1000

  where |n| is the modulus/absolute value of n
  e.g. |11| = 11 and |−4| = 4
  Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
  
  Answer: -59231 Completed on Tue, 14 Oct 2014, 21:49
  https://projecteuler.net/problem=27
  
  @author Botu Sun
'''

import math

def IsPrime(n):
  if n < 2: return False
  if n == 2: return True
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True
  
max_number = 1
max_mult = 0
for a in xrange(-999, 1000, 2):
  for b in xrange(-999, 1000, 2):
    i = 0
    while IsPrime(i * i + a * i + b):
      i += 1
    if i > max_number:
      max_number = i
      max_mult = a * b
      
print max_mult
