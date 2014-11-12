# -*- coding: utf-8 -*-
'''
  Prime permutations
  Problem 49
  
  The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

  There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

  What 12-digit number do you form by concatenating the three terms in this sequence?

  Answer: 296962999629 Completed on Wed, 22 Oct 2014, 13:16
  https://projecteuler.net/problem=49
  
  @author Botu Sun
'''

import math

def IsPrime(n):
  if n < 2: return False
  if n == 2: return True
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def Recursion(bit_map, list, i, j, k, n):
  if n == 3:
    if list[j] - list[i] == list[k] - list[j]:
      print ''.join(str(list[i]) + str(list[j]) + str(list[k]))
  elif n == 0:
    for x in xrange(0, len(bit_map)):
      bit_map[x] = False
      i = x
      Recursion(bit_map, list, i, j, k, n + 1)
      bit_map[x] = True
  elif n == 1:
    for x in xrange(i + 1, len(bit_map)):
      bit_map[x] = False
      j = x
      Recursion(bit_map, list, i, j, k, n + 1)
      bit_map[x] = True
  elif n == 2:
    for x in xrange(j + 1, len(bit_map)):
      bit_map[x] = False
      k = x
      Recursion(bit_map, list, i, j, k, n + 1)
      bit_map[x] = True
      
  
def ValidSequence(list):
  bit_map = [True] * len(list)
  Recursion(bit_map, list, 0, 0, 0, 0)
  
map = {}
for i in xrange(1000, 10000):
  if IsPrime(i):
    key = ''.join(sorted(str(i)))
    if map.has_key(key):
      map[key].append(i)
    else:
      map[key] = [i]

for i in map.values():
  if len(i) >= 3 and ValidSequence(i):
    exit(0)