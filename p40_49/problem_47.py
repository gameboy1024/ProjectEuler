# -*- coding: utf-8 -*-
'''
  Distinct primes factors
  Problem 47
  
  The first two consecutive numbers to have two distinct prime factors are:

  14 = 2 × 7
  15 = 3 × 5

  The first three consecutive numbers to have three distinct prime factors are:

  644 = 2² × 7 × 23
  645 = 3 × 5 × 43
  646 = 2 × 17 × 19.

  Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

  Answer: 134043 Completed on Tue, 21 Oct 2014, 23:55
  https://projecteuler.net/problem=47
  
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

primes = []
for i in xrange(2, 100000):
  if IsPrime(i):
    primes.append(i)

def ValidNumber(n):
  p = n
  global primes
  factors = {}
  for prime in primes:
    while (n % prime == 0):
      n /= prime
      factors[prime] = True
    if n <= prime:
      break
  if len(factors.keys()) == 4:
    return True
  return False

i = 2 * 3 * 5 * 7
w = ValidNumber(i)
x = ValidNumber(i + 1)
y = ValidNumber(i + 2)
z = ValidNumber(i + 3)

while (True):
  if w and x and y and z:
    print i
    exit(0)
  if not z:
    w = ValidNumber(i + 4)
    x = ValidNumber(i + 5)
    y = ValidNumber(i + 6)
    z = ValidNumber(i + 7)
    i += 4
  elif not y:
    w = z
    x = ValidNumber(i + 4)
    y = ValidNumber(i + 5)
    z = ValidNumber(i + 6)
    i += 3
  elif not x:
    w = y
    x = z
    y = ValidNumber(i + 4)
    z = ValidNumber(i + 5)
    i += 2
  else:
    w = x
    x = y
    y = z
    z = ValidNumber(i + 4)
    i += 1