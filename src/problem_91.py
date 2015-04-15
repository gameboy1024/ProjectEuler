# -*- coding: utf-8 -*-
'''
  Right triangles with integer coordinates
  Problem 91
  
  The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and 
  are joined to the origin, O(0,0), to form ΔOPQ.
  
  
  There are exactly fourteen triangles containing a right angle that can be 
  formed when each co-ordinate lies between 0 and 2 inclusive; that is,
  0 ≤ x1, y1, x2, y2 ≤ 2.
  
  
  Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

  Answer: 14234 Completed on Wed, 15 Apr 2015, 16:29
  https://projecteuler.net/problem=91
  
  @author Botu Sun
'''

n = 50
result = 0
# Right angle at 0, 0:
result += n ** 2
# Right angle at y axis or x axis other than 0, 0:
result += n ** 2 * 2
# Right angle at somewhere in the middle:
# x1, y1 is always the right angle point of the triangle
for x1 in xrange(1, n + 1):
  for y1 in xrange(1, n + 1):
    for x2 in xrange(0, n + 1):
      if x2 == x1: continue
      for y2 in xrange(0, n + 1):
        # Only consider those in 2rd and 4th quadrant
        if (x2 - x1) * (y2 - y1) > 0: continue
        # If they are perpendicular, increment result
        if abs((y1 * 1.0 / x1) * (y2 - y1) * 1.0 / (x2 - x1) + 1) < 1E-10:
          result += 1

print result