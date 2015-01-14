# -*- coding: utf-8 -*-
'''
  Counting summations
  Problem 76
  It is possible to write five as a sum in exactly six different ways:

  4 + 1
  3 + 2
  3 + 1 + 1
  2 + 2 + 1
  2 + 1 + 1 + 1
  1 + 1 + 1 + 1 + 1

  How many different ways can one hundred be written as a sum of at least two 
  positive integers?

  Answer: 190569291 Completed on Tue, 6 Jan 2015, 16:13
  https://projecteuler.net/problem=76
  
  @author Botu Sun
'''

def Function(x, y, map):
  if x <= 1 or y <= 1:
    return 1
  if (x, y) in map:
    return map[(x, y)]
  sum = 0
  limit = x - y - 1 if x > y else -1
  for i in xrange(x - 1, limit, -1):
    sum += Function(i, x - i, map)
  map[(x, y)] = sum
  return sum

map = {}
print Function(100, 99, map)