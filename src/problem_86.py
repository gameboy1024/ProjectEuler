# -*- coding: utf-8 -*-
'''
  Cuboid route
  Problem 86
  
  A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
  fly, F, sits in the opposite corner. By travelling on the surfaces of the room
  the shortest "straight line" distance from S to F is 10 and the path is shown 
  on the diagram.


  However, there are up to three "shortest" path candidates for any given cuboid
  and the shortest route doesn't always have integer length.

  It can be shown that there are exactly 2060 distinct cuboids, ignoring 
  rotations, with integer dimensions, up to a maximum size of M by M by M, for 
  which the shortest route has integer length when M = 100. This is the least 
  value of M for which the number of solutions first exceeds two thousand; the 
  number of solutions when M = 99 is 1975.

  Find the least value of M such that the number of solutions first exceeds one 
  million.

  Answer: 1818 Completed on Sun, 29 Mar 2015, 21:50
  https://projecteuler.net/problem=86
  
  @author Botu Sun
'''

# This is not my original solution, actually I solved this problem with much
# more sophisticated brute force solution, which is easily beaten by this one.
# Code by mereandor on projecteuler.net

from itertools import count
from math import sqrt

x = 0
# a is M, and the longest edge during this iteration
for a in count(1):
  # s is the sum of the other two edges, which cannot exceed 2a
	for s in range(1, 2 * a + 1):
		z = sqrt(a ** 2 + s ** 2)
		if int(z) == z:
		  # The possible splits is determined here, we have to be sure a is largest.
			x += min(a, s - 1) - (s - 1) / 2
	if x > 1000000:
		print a, x
		exit()