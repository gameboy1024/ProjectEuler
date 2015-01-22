# -*- coding: utf-8 -*-
'''
  Prime summations
  Problem 77
  It is possible to write ten as the sum of primes in exactly five different 
  ways:

  7 + 3
  5 + 5
  5 + 3 + 2
  3 + 3 + 2 + 2
  2 + 2 + 2 + 2 + 2

  What is the first value which can be written as the sum of primes in over five
  thousand different ways?

  Answer: 71 Completed on Thu, 22 Jan 2015, 11:59
  https://projecteuler.net/problem=77
  
  @author Botu Sun
'''

from lib.math_utils import PrimeChecker

prime_checker = PrimeChecker(1E5)
def Function(x, y, map, prime_checker):
  if x == 0: return 1
  if x < 2: return 0
  if (x, y) in map: return map[(x, y)]
  sum = 0
  for p in prime_checker.get_prime_list():
    if p <= x and p <= y:
      tmp = Function(x - p, p, map, prime_checker)
      sum += tmp
    else:
      break
  map[(x, y)] = sum
  return sum

map = {}

i = 1
while (Function(i, i - 1, map, prime_checker) <= 5000):
  i += 1

print i

