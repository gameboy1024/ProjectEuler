# -*- coding: utf-8 -*-
'''
  Integer right triangles
  Problem 39

  If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

  {20,48,52}, {24,45,51}, {30,40,50}

  For which value of p ≤ 1000, is the number of solutions maximised?
  
  Answer: 840 Completed on Mon, 20 Oct 2014, 22:28
  https://projecteuler.net/problem=39
  
  @author Botu Sun
'''

import math

max_count = 0
max_number = 0
for i in xrange(12, 1001):
  count = 0
  # sqrt(2) ~ 1.4142
  for j in xrange(int(0.4142 * i), int(0.5 * i + 1)):
    for k in xrange(1, j):
      if i == 120 and j == 50 and k == 30:
        print 'haha'
      if j * j == k * k + (i - j - k) * (i - j - k):
        print i, j, k, j - k
        count += 1
  if count > max_count:
    max_count = count
    max_number = i
    
print max_number