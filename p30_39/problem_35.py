# -*- coding: utf-8 -*-
'''
  Circular primes
  Problem 35
  
  The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

  There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

  How many circular primes are there below one million?
  
  Answer: 55 Completed on Thu, 16 Oct 2014, 21:10
  https://projecteuler.net/problem=35
  
  @author Botu Sun
'''

import math

def IsAllOdd(n):
  while n != 0:
    if n % 2 == 0:
      return False
    else:
      n /= 10
  return True

def IsPrime(n):
  if n == 2: return True
  for i in xrange(3, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def Rotate(n):
  return n / 10 + n % 10 * int(math.pow(10, math.ceil(math.log10(n)) - 1))
  
count = 1 # 2 is special!
for i in xrange(2, int(1E6)):
  if IsAllOdd(i) and IsPrime(i):
    tmp = Rotate(i)
    while tmp != i and IsPrime(tmp):
      tmp = Rotate(tmp)
    if tmp == i:
      count += 1
      
print count
  