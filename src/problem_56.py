# -*- coding: utf-8 -*-
'''
  Powerful digit sum
  Problem 56
  
  A googol (10100) is a massive number: one followed by one-hundred zeros; 
  100100 is almost unimaginably large: one followed by two-hundred zeros. 
  Despite their size, the sum of the digits in each number is only 1.

  Considering natural numbers of the form, ab, where a, b < 100, what is the 
  maximum digital sum?

  Answer: 972 Completed on Thu, 13 Nov 2014, 15:29
  https://projecteuler.net/problem=56
  
  @author Botu Sun
'''

from lib import math_utils as math
  
max = 0
for i in xrange(2, 101):
  for j in xrange(2, 101):
    tmp = sum(math.power_list(i, j))
    if tmp > max:
      max = tmp
print max