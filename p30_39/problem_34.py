# -*- coding: utf-8 -*-
'''
  Digit factorials
  Problem 34
  
  145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

  Find the sum of all numbers which are equal to the sum of the factorial of their digits.

  Note: as 1! = 1 and 2! = 2 are not sums they are not included.
  
  Answer: 40730 Completed on Wed, 15 Oct 2014, 23:50
  https://projecteuler.net/problem=34
  
  @author Botu Sun
'''

import math

total = 0
for i in xrange(3, int(362880 / 8)):
  sum = 0
  remain = i
  while remain != 0:
    sum += math.factorial(remain % 10)
    remain = int(remain / 10)
  if sum == i:
    total += i
    continue
      
print total