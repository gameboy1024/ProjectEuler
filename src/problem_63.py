# -*- coding: utf-8 -*-
'''
  Powerful digit counts
  Problem 63
  The 5-digit number, 16807=75, is also a fifth power. Similarly, the 
  9-digit number, 134217728=89, is a ninth power.

  How many n-digit positive integers exist which are also an nth power?

  Answer: 49 Completed on Mon, 17 Nov 2014, 16:58
  https://projecteuler.net/problem=63
  
  @author Botu Sun
'''

import math
from lib import math_utils

count = 1

i = 2
for i in xrange(2, 10):
  j = 1
  while True:
    power = math_utils.power_list(i, j)
    if len(power) == j:
      count += 1
    elif len(power) - len(str(j)) > int(math.log10(i)):
      break
    j += 1
  i += 1
  
print count
