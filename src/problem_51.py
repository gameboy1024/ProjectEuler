# -*- coding: utf-8 -*-
'''
  Prime digit replacements
  Problem 51
  
  By replacing the 1st digit of the 2-digit number *3, it turns out that
  six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all 
  prime.

  By replacing the 3rd and 4th digits of 56**3 with the same digit, this
  5-digit number is the first example having seven primes among the ten 
  generated numbers, yielding the family: 56003, 56113, 56333, 56443, 
  56663, 56773, and 56993. Consequently 56003, being the first member of
  this family, is the smallest prime with this property.

  Find the smallest prime which, by replacing part of the number (not 
  necessarily adjacent digits) with the same digit, is part of an eight 
  prime value family.

  Answer: 121313 Completed on Tue, 28 Oct 2014, 11:21.37
  https://projecteuler.net/problem=51
  
  @author Botu Sun
'''

import math

LIMIT = 3 * int(1E6)
PERM = [[(0,)]]
for i in xrange(1, 8):
  next = [(i,)]
  for perm in PERM[i - 1]:
    next.append(perm)
    next.append(perm + (i,))
  PERM.append(next)

def GeneratePrimes(limit):
  map = {}
  primes = []
  numbers = [True] * (limit + 1)
  for i in xrange(2, limit / 2 + 1):
    if numbers[i] == True:
      j = i * 2
      while (j <= limit):
        numbers[j] = False
        j += i
  for i in xrange(2, limit + 1):
    if numbers[i] == True:
      map[i] = True
      primes.append(i)
  return map, primes

map, primes = GeneratePrimes(LIMIT)

def ValidNumber(map, n, locations, digit):
  '''Valid if the family number is 8 and if we change some digits.'''
  for perm in PERM[len(locations) - 1 ]:
    count = 0
    first = None
    step = int(sum(i for i in [math.pow(10, locations[d]) for d in perm]))
    start_number = n - step * digit
    for i in xrange(0, 10):
      candidate = start_number + step * i
      if map.has_key(candidate) and len(str(candidate)) == len(str(n)):
        if not first:
          first = start_number + step * i
        count += 1
    if count == 8:
      print first
      exit(0)
  return
  
for i in primes:
  digit_count = [[], [], [], [], [], [], [], [], [], []]
  for d in xrange(0, len(str(i))):
    digit_count[int(str(i)[d])].append(len(str(i)) - d - 1)
  for d in xrange(0, 10):
    if len(digit_count[d]) != 0:
      ValidNumber(map, i, digit_count[d], d)

