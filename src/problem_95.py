# -*- coding: utf-8 -*-
'''
  Amicable chains
  Problem 95
  
  The proper divisors of a number are all the divisors excluding the number 
  itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the 
  sum of these divisors is equal to 28, we call it a perfect number.
  
  Interestingly the sum of the proper divisors of 220 is 284 and the sum of the 
  proper divisors of 284 is 220, forming a chain of two numbers. For this 
  reason, 220 and 284 are called an amicable pair.
  
  Perhaps less well known are longer chains. For example, starting with 12496, 
  we form a chain of five numbers:
  
  12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)
  
  Since this chain returns to its starting point, it is called an amicable 
  chain.
  
  Find the smallest member of the longest amicable chain with no element 
  exceeding one million.

  Answer: 14316 Completed on Wed, 29 Apr 2015, 16:22
  https://projecteuler.net/problem=95
  
  @author Botu Sun
'''
from lib.math_utils import PrimeFactorsGenerator

LIMIT = int(1E6)

prime_factors_generator = PrimeFactorsGenerator(LIMIT)
factors = prime_factors_generator.get_prime_factors()
print 'Prime factors done!'

divisors = {1: set([1])}
for i in xrange(2, LIMIT):
  # Make a copy of divisors of one of its divisor
  divisors[i] = divisors[i / factors[i][-1]].copy()
  # For every divisors of its divisor, multiply it with the new factor
  for d in divisors[i / factors[i][-1]]:
    divisors[i].add(d * factors[i][-1])
  divisors[i].add(i / factors[i][-1])
  if i in divisors[i]:
    divisors[i].remove(i)
print 'Divisors done!'
factors = None

divisors_sum = {1: 1}
for k, v in divisors.items():
  divisors_sum[k] = sum(v)
print 'Divisors sum done!'
divisors = None

max_start = 0
max_length = 0
for i in xrange(2, LIMIT):
  checked = set([i])
  start = i
  length = 1
  i = divisors_sum[i]
  checked.add(i)
  while i != start:
    if i > LIMIT:
      break
    i = divisors_sum[i]
    if i in checked:
      break
    checked.add(i)
    length += 1
  if i == start and length > max_length:
    max_length = length
    max_start = start
print max_start, max_length