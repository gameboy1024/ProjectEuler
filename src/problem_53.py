# -*- coding: utf-8 -*-
'''
  Combinatoric selections
  Problem 53
  
  There are exactly ten ways of selecting three from five, 12345:

  123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

  In combinatorics, we use the notation, 5C3 = 10.

  In general,

  nCr =	n! / r!(n−r)!, where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
  It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

  How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are 
  greater than one-million?

  Answer: 4075 Completed on Tue, 28 Oct 2014, 21:05.17
  https://projecteuler.net/problem=53
  
  @author Botu Sun
'''

count = 0

def Calculate(n, r):
  global count
  if n - r < r:
    r = n - r
  end = n - r
  mul = 1
  denom = 2
  for i in xrange(end + 1, n + 1):
    mul *= i
    while (denom <= r and mul % denom == 0):
      mul /= denom
      denom += 1
    if mul > 1E6:
      count += 1
      return
  if mul > 1E6:
    count += 1

for n in xrange(23, 101):
  for r in xrange(0, n + 1):
    Calculate(n, r)
    
print count