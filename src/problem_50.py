# -*- coding: utf-8 -*-
'''
  Consecutive prime sum
  Problem 50
  
  The prime 41, can be written as the sum of six consecutive primes:

  41 = 2 + 3 + 5 + 7 + 11 + 13
  This is the longest sum of consecutive primes that adds to a prime below 
  one-hundred.

  The longest sum of consecutive primes below one-thousand that adds to a prime, 
  contains 21 terms, and is equal to 953.

  Which prime, below one-million, can be written as the sum of the most 
  consecutive primes?

  Answer: 997651 Completed on Wed, 22 Oct 2014, 15:23.46
  https://projecteuler.net/problem=50
  
  @author Botu Sun
'''

import math

LIMIT = int(1E6)

def GeneratePrimes(limit):
  map = {}
  primes = []
  numbers = [True] * (limit + 1)
  for i in xrange(2, limit / 2 + 1):
    if numbers[i] == True:
      j = i * 2
      while (j <= limit):
        numbers[j] = False
        j += i
  for i in xrange(2, limit + 1):
    if numbers[i] == True:
      map[i] = True
      primes.append(i)
  return map, primes

map, primes = GeneratePrimes(LIMIT)
print 'Primes list and dict constructed!'

length = len(primes)
while (True):
  if length % 1000 == 0:
    print '\r' + str(length),
  for i in xrange(0, len(primes) - length + 1):
    sum = 0
    for j in xrange(i, i + length):
      sum += primes[j]
      if sum >= LIMIT:
        break
    if sum < LIMIT:
      if map.has_key(sum):
        print ''
        print sum
        exit(0)
    else:
      break
  length -= 1
    
