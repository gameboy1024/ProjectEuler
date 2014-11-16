# -*- coding: utf-8 -*-
'''
  Prime pair sets
  Problem 60
  The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
  and concatenating them in any order the result will always be prime. For 
  example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four 
  primes, 792, represents the lowest sum for a set of four primes with this 
  property.

  Find the lowest sum for a set of five primes for which any two primes 
  concatenate to produce another prime.

  Answer: 26033 Completed on Fri, 14 Nov 2014, 18:19
  My solution to this problem is far from optimal, it took several minutes to
  get the right value if the SUM_LIMIT is higher. Better solutions can be found 
  on the problem thread.
  https://projecteuler.net/problem=60
  
  @author Botu Sun
'''

from lib import math_utils as math
    
def concatenate(a, b):
  tmp = 1
  while tmp < b:
    tmp *= 10
  return a * tmp + b

LIMIT = 10000
SUM_LIMIT = 30000
numbers = [0] * 5
prime_checker = math.PrimeChecker(1E7 - 1)
def valid_set(prime_checker, SUM_LIMIT, numbers, n):
  if sum(numbers[0:n + 1]) > SUM_LIMIT:
    return 2
  for i in xrange(0, n):
    if (not prime_checker.is_prime(concatenate(numbers[i], numbers[n])) or
        not prime_checker.is_prime(concatenate(numbers[n], numbers[i]))):
      return 1
  if n == 4:
    total = sum(numbers)
    if SUM_LIMIT > total:
      SUM_LIMIT = total
    print numbers
    print sum(numbers)
  return 0

prime_list = prime_checker.get_prime_list()

for i in xrange(1, LIMIT):
  numbers[0] = prime_list[i]
  # print i
  for j in xrange(i + 1, LIMIT):
    numbers[1] = prime_list[j]
    # print ' ' + str(j)
    result_j = valid_set(prime_checker, SUM_LIMIT, numbers, 1)
    if result_j == 1:
      continue
    elif result_j == 2:
      break
    for k in xrange(j + 1, LIMIT):
      numbers[2] = prime_list[k]
      # print '  ' + str(k)
      result_k = valid_set(prime_checker, SUM_LIMIT, numbers, 2)
      if result_k == 1:
        continue
      elif result_k == 2:
        break
      for m in xrange(k + 1, LIMIT):
        numbers[3] = prime_list[m]
        result_m = valid_set(prime_checker, SUM_LIMIT, numbers, 3)
        if result_m == 1:
          continue
        elif result_m == 2:
          break
        for l in xrange(m + 1, LIMIT):
          numbers[4] = prime_list[l]
          result_n = valid_set(prime_checker, SUM_LIMIT, numbers, 4)
          if result_n == 1:
            continue
          elif result_n == 2:
            break
print i, j, k, m, l
print SUM_LIMIT