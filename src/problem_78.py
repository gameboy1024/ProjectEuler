# -*- coding: utf-8 -*-
'''
  Coin partitions
  Problem 78
  Let p(n) represent the number of different ways in which n coins can be 
  separated into piles. For example, five coins can separated into piles in 
  exactly seven different ways, so p(5)=7.

  OOOOO
  OOOO   O
  OOO   OO
  OOO   O   O
  OO   OO   O
  OO   O   O   O
  O   O   O   O   O
  Find the least value of n for which p(n) is divisible by one million.

  Answer: 55374 Completed on Tue, 27 Jan 2015, 18:30
  https://projecteuler.net/problem=78
  
  @author Botu Sun
'''

import math

# Recursion and caching.
def P(n, map):
  if n < 0: return 0
  if map[n]: return map[n]
  sum = 0
  for i in xrange(1, int(math.sqrt(n)) + 1):
    sum += (-1) ** (i + 1) * (
        P(n - i * (3 * i - 1) / 2, map) + P(n - i * (3 * i + 1) / 2, map))
  sum %= 10000000
  map[n] = sum
  return sum

map = [1]
map.extend([0] * 100000)

i = 1
while(P(i, map) % 1000000 != 0):
  i += 1
print i