# -*- coding: utf-8 -*-
'''
  Counting fractions in a range
  Problem 73
  
  Consider the fraction, n/d, where n and d are positive integers. If n<d and 
  HCF(n,d)=1, it is called a reduced proper fraction.

  If we list the set of reduced proper fractions for d ≤ 8 in ascending order of
  size, we get:

  1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 
  5/7, 3/4, 4/5, 5/6, 6/7, 7/8

  It can be seen that there are 3 fractions between 1/3 and 1/2.

  How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper
  fractions for d ≤ 12,000?

  Answer: 7295372 Completed on Wed, 3 Dec 2014, 14:58
  https://projecteuler.net/problem=73
  
  Better solutions can be found on the overview of this problem.
  
  @author Botu Sun
'''

import math
from lib import math_utils
from lib import list_utils

LIMIT = 12000

total = 0

interval = (1.0 / 3, 1.0 / 2)

for i in xrange(2, LIMIT + 1):
  for j in xrange(
      int(math.floor(interval[0] * i)) + 1, int(math.ceil(interval[1] * i))):
    if math_utils.gcd(i, j) == 1:
      total += 1

print total
