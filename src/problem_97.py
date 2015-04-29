# -*- coding: utf-8 -*-
'''
  Large non-Mersenne prime
  Problem 97
  
  The first known prime found to exceed one million digits was discovered in 
  1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 
  2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have 
  been found which contain more digits.
  
  However, in 2004 there was found a massive non-Mersenne prime which contains 
  2,357,207 digits: 28433×2^7830457+1.
  
  Find the last ten digits of this prime number.

  Answer: 8739992577 Completed on Thu, 30 Apr 2015, 00:17
  https://projecteuler.net/problem=97
  
  @author Botu Sun
'''

LIMIT = 7830457
MULTIPLIER = 1000
result = 1
i = 0
while i < LIMIT / MULTIPLIER:
  result *= 2 ** MULTIPLIER
  result %= 10000000000
  i += 1
result *= 2 ** (LIMIT % MULTIPLIER)
# print result
print (result * 28433 + 1) % 10000000000