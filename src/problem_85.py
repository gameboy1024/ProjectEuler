# -*- coding: utf-8 -*-
'''
  Counting rectangles
  Problem 85
  By counting carefully it can be seen that a rectangular grid measuring 3 by 2 
  contains eighteen rectangles:

  [the graph example can be found on the original page]

  Although there exists no rectangular grid that contains exactly two million 
  rectangles, find the area of the grid with the nearest solution.

  Answer: 2772 Completed on Thu, 29 Jan 2015, 11:49
  https://projecteuler.net/problem=85
  
  @author Botu Sun
'''
LIMIT = 2000000

def f(x, y):
  return x * (x + 1) * y * (y + 1) / 4

upper_limit = 0
above_limit = 0
nearest_distance = LIMIT
nearest_x = 0
nearest_y = 0
x = 1
y = 1

while f(x, y) < LIMIT:
  while upper_limit < LIMIT:
    upper_limit = f(x, y)
    y += 1
  lower_limit = f(x, y - 2)
  if abs(upper_limit - LIMIT) < nearest_distance:
    nearest_distance = abs(upper_limit - LIMIT)
    nearest_x = x
    nearest_y = y - 1
  if abs(lower_limit - LIMIT) < nearest_distance:
    nearest_distance = abs(lower_limit - LIMIT)
    nearest_x = x
    nearest_y = y - 2
  x += 1
  y = 1
  upper_limit = 0

tmp = f(x, y)
if abs(tmp - LIMIT) < nearest_distance:
    nearest_distance = abs(tmp - LIMIT)
    nearest_x = x
    nearest_y = y

print nearest_x * nearest_y, '=', nearest_x, '*', nearest_y
