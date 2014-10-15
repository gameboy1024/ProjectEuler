# -*- coding: utf-8 -*-
'''
  Coin sums
  Problem 31
  
  In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
  It is possible to make £2 in the following way:

  1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
  How many different ways can £2 be made using any number of coins?
  
  Answer: 73682 Completed on Wed, 15 Oct 2014, 22:01
  https://projecteuler.net/problem=31
  
  @author Botu Sun
'''

count = 0
a = [200, 100, 50, 20, 10, 5, 2, 1]

def recursion(a, i, remain):
  global count
  if i == 8 and remain == 0:
    count += 1
  if i == 8 or remain < 0:
    return
  while remain >= 0:
    recursion(a, i + 1, remain)
    remain -= a[i]

recursion(a, 0, 200)
print count