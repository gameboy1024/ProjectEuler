# -*- coding: utf-8 -*-
'''
  Number spiral diagonals
  Problem 28
  
  Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

  21 22 23 24 25
  20  7  8  9 10
  19  6  1  2 11
  18  5  4  3 12
  17 16 15 14 13

  It can be verified that the sum of the numbers on the diagonals is 101.

  What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
  
  Answer: 669171001 Completed on Tue, 14 Oct 2014, 22:03
  https://projecteuler.net/problem=28
  
  @author Botu Sun
'''

sum = 1
step = 1
previous = 1
while step < 1001 / 2 + 1:
  sum += 4 * previous + 4 * step * 2 + 3 * step * 2 + 2 * step * 2 + step * 2
  previous += 4 * step * 2
  step += 1
  
print sum
