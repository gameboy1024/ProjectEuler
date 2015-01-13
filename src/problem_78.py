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

  Answer: 190569291 Completed on Tue, 6 Jan 2015, 16:13
  https://projecteuler.net/problem=78
  
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
i = 0
while Function(i, i, map) % 1000000 != 0:
  i += 1
  print i
print i