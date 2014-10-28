# -*- coding: utf-8 -*-
'''
  Permuted multiples
  Problem 52

  It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

  Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

  Answer: 142857 Completed on Tue, 28 Oct 2014, 16:57.07
  https://projecteuler.net/problem=52
  
  @author Botu Sun
'''

i = 1
while(True):
  a = []
  self = ''.join(sorted(str(i)))
  flag = True
  for mul in xrange(2, 7):
    if self != ''.join(sorted(str(mul * i))):
      flag = False
  if flag:
    print i
    exit(0)
  i += 1