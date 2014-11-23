# -*- coding: utf-8 -*-
'''
  Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
  each line adding to nine.

  ...[The figure is in the web page]
  
  Working clockwise, and starting from the group of three with the numerically 
  lowest external node (4,3,2 in this example), each solution can be described 
  uniquely. For example, the above solution can be described by the set: 4,3,2; 
  6,2,1; 5,1,3.

  It is possible to complete the ring with four different totals: 9, 10, 11, and
  12. There are eight solutions in total.

  Total	Solution Set
  9	4,2,3; 5,3,1; 6,1,2
  9	4,3,2; 6,2,1; 5,1,3
  10	2,3,5; 4,5,1; 6,1,3
  10	2,5,3; 6,3,1; 4,1,5
  11	1,4,6; 3,6,2; 5,2,4
  11	1,6,4; 5,4,2; 3,2,6
  12	1,5,6; 2,6,4; 3,4,5
  12	1,6,5; 3,5,4; 2,4,6
  By concatenating each group it is possible to form 9-digit strings; the 
  maximum string for a 3-gon ring is 432621513.

  Using the numbers 1 to 10, and depending on arrangements, it is possible to 
  form 16- and 17-digit strings. What is the maximum 16-digit string for a 
  "magic" 5-gon ring?

  Answer: 6531031914842725 Completed on Sun, 23 Nov 2014, 15:53
  https://projecteuler.net/problem=68
  
  @author Botu Sun
'''

import math
from lib import math_utils

"""
  Let's number the points in the ring and use brute force, since it's O(10!)
  time. The actual time is much smaller since we check as soon as two groups are
  ready.
              0
                 1    3   
              8     2
           9   6  4    5
                 7 
"""
groups = [[0, 1, 2], [3, 2, 4], [5, 4, 6], [7, 6, 8], [9, 8, 1]]
candidates = []
def validate_combination(numbers, slot_bitmap):
  total = None
  for g in groups:
    if sum(slot_bitmap[i] for i in g) == 3:
      if not total:
        total = sum(numbers[i] for i in g)
      elif total != sum(numbers[i] for i in g):
        return False
  return True
  
numbers_bitmap = [True] * 10
slot_bitmap = [False] * 10
numbers = [0] * 10

def output(numbers):
  global groups
  min = sorted([(numbers[groups[i][0]], i) for i in xrange(0, 5)])[0][1]
  result = ''
  for i in xrange(min, min + len(groups)):
    result += ''.join([str(numbers[j]) for j in groups[i % len(groups)]])
  return result

def recursion(numbers, numbers_bitmap, n):
  if n == 10:
    result = output(numbers)
    if len(result) == 16:
      global candidates
      candidates.append(result)
    
  for i in xrange(0, 10):
    if numbers_bitmap[i] == False:
      continue
    numbers_bitmap[i] = False
    slot_bitmap[n] = True
    numbers[n] = i + 1
    if validate_combination(numbers, slot_bitmap):
      recursion(numbers, numbers_bitmap, n + 1)
    numbers_bitmap[i] = True
    slot_bitmap[n] = False

recursion(numbers, numbers_bitmap, 0)
print sorted(candidates)[-1]