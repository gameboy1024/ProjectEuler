# -*- coding: utf-8 -*-
'''
  Cubic permutations
  Problem 62
  The cube, 41063625 (3453), can be permuted to produce two other cubes: 
  56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube 
  which has exactly three permutations of its digits which are also cube.

  Find the smallest cube for which exactly five permutations of its digits are 
  cube.

  Answer: 127035954683 Completed on Mon, 17 Nov 2014, 11:04
  https://projecteuler.net/problem=62
  
  @author Botu Sun
'''

import sys
from lib import math_utils as math

LIMIT = 10000
map = {}
min = None

for i in xrange(1, LIMIT):
  cube = math.power_list(i, 3)
  key = ''.join([str(n) for n in sorted(cube)])
  if key not in map:
    map[key] = [cube]
  else:
    map[key].append(cube)
  
for i, v in map.items():
  if len(v) == 5:
    value = ''.join([str(m) for m in v[0]])
    if not min or min > value:
      min = value
      
print min