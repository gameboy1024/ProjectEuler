# -*- coding: utf-8 -*-
'''
  Digit fifth powers
  Problem 30
  
  Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

  1634 = 14 + 64 + 34 + 44
  8208 = 84 + 24 + 04 + 84
  9474 = 94 + 44 + 74 + 44
  As 1 = 14 is not a sum it is not included.

  The sum of these numbers is 1634 + 8208 + 9474 = 19316.

  Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
  
  Answer: 443839 Completed on Wed, 15 Oct 2014, 21:23
  https://projecteuler.net/problem=30
  
  @author Botu Sun
'''

import math

total = 0
for i in xrange(2, int(1E6)):
  remain = i
  sum = 0
  while remain != 0:
    sum += math.pow(remain % 10, 5)
    remain = int(remain / 10)
    if sum > i:
      break
  if i == sum:
    total += i
    
print total
    