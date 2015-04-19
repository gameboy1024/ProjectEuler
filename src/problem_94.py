# -*- coding: utf-8 -*-
'''
  Almost equilateral triangles
  Problem 94
  
  It is easily proved that no equilateral triangle exists with integral length 
  ides and integral area. However, the almost equilateral triangle 5-5-6 has an 
  area of 12 square units.
  
  We shall define an almost equilateral triangle to be a triangle for which two 
  sides are equal and the third differs by no more than one unit.
  
  Find the sum of the perimeters of all almost equilateral triangles with 
  integral side lengths and area and whose perimeters do not exceed one billion 
  (1,000,000,000).

  Answer: 518408346 Completed on Sun, 19 Apr 2015, 22:37
  https://projecteuler.net/problem=94
  
  @author Botu Sun
'''
# This is not a good solution at all.. the brute-force is veeeeeeeery slow...
import math

LIMIT = int(1E9)
total = 0
i = 5
while True:
  if 3 * i - 1 > LIMIT:
      print total
      exit()
  a = i ** 2 - ((i - 1) / 2) ** 2
  b = i ** 2 - ((i + 1) / 2) ** 2
  if int(math.sqrt(a)) ** 2 == a:
    print i, i, i - 1
    total += i * 3 - 1
    i *= 3
  if int(math.sqrt(b)) ** 2 == b:
    print i, i, i + 1
    total += i * 3 + 1
    i *= 3
  i += 2