# -*- coding: utf-8 -*-
'''
  Odd period square roots
  Problem 64
  All square roots are periodic when written as continued fractions and can be 
  written in the form:

  √N = a0 +	1
        a1 + 1
          a2 + 1
            a3 + ...
  For example, let us consider √23:

  ...[refer to problem page as the formats in plain text aren't pretty]

  It can be seen that the sequence is repeating. For conciseness, we use the 
  notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats 
  indefinitely.

  The first ten continued fraction representations of (irrational) square roots 
  are:

  √2=[1;(2)], period=1
  √3=[1;(1,2)], period=2
  √5=[2;(4)], period=1
  √6=[2;(2,4)], period=2
  √7=[2;(1,1,1,4)], period=4
  √8=[2;(1,4)], period=2
  √10=[3;(6)], period=1
  √11=[3;(3,6)], period=2
  √12= [3;(2,6)], period=2
  √13=[3;(1,1,1,1,6)], period=5

  Exactly four continued fractions, for N ≤ 13, have an odd period.

  How many continued fractions for N ≤ 10000 have an odd period?

  Answer: 1322 Completed on Tue, 18 Nov 2014, 23:40
  https://projecteuler.net/problem=64
  
  @author Botu Sun
'''

import math
from lib import math_utils

def get_period(n):
  # The idea comes from:
  # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section7
  nearest_root = int(math.sqrt(n))
  c = -nearest_root
  d = 1
  period = 0
  
  while True:
    nearest_root = int(math.sqrt((math.sqrt(n) + c) / d))
    c -=  nearest_root * d
    d = (n - c * c) / d
    c = -c
    period += 1
    if d == 1:
      return period

count = 0
for i in xrange(2, 10001):
  if math.pow(int(math.sqrt(i)), 2) == i:
    continue
  if not math_utils.is_even(get_period(i)):  
    count += 1
print count