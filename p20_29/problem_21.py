# -*- coding: utf-8 -*-
'''
  Amicable numbers
  Problem 21
  
  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
  If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

  Evaluate the sum of all the amicable numbers under 10000.
  
  Answer: 31626 Completed on Mon, 13 Oct 2014, 23:36
  https://projecteuler.net/problem=21
  
  @author Botu Sun
'''

map = {}
for i in xrange(1, 10001):
  tmp = 0
  for j in xrange(1, i / 2 + 1):
    if i % j == 0:
      tmp += j
  map[i] = tmp

sum = 0
for key in map.keys():
  if map.has_key(map[key]) and key != map[key] and map[map[key]] == key:
    sum += key

print sum