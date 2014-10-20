# -*- coding: utf-8 -*-
'''
  Pandigital prime
  Problem 41
  
  We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

  What is the largest n-digit pandigital prime that exists?
  
  Answer: 7652413 Completed on Mon, 20 Oct 2014, 23:53
  https://projecteuler.net/problem=41
  
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

max = 0
def Recursion(a, current, n, total):
  if n == total and IsPrime(current):
    print current
    exit()
       
  for i in xrange(0, total):
    if a[i] == False:
      tmp = current
      a[i] = True
      tmp *= 10
      tmp += total - i
      Recursion(a, tmp, n + 1, total)
      a[i] = False
      
for i in xrange(9, 1, -1):
  a = [False] * i
  Recursion(a, 0, 0, i)