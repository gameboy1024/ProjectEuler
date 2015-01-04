# -*- coding: utf-8 -*-
'''
  Digit factorial chains
  Problem 74
  The number 145 is well known for the property that the sum of the factorial of
  its digits is equal to 145:

  1! + 4! + 5! = 1 + 24 + 120 = 145

  Perhaps less well known is 169, in that it produces the longest chain of 
  numbers that link back to 169; it turns out that there are only three such 
  loops that exist:

  169 → 363601 → 1454 → 169
  871 → 45361 → 871
  872 → 45362 → 872

  It is not difficult to prove that EVERY starting number will eventually get 
  stuck in a loop. For example,

  69 → 363600 → 1454 → 169 → 363601 (→ 1454)
  78 → 45360 → 871 → 45361 (→ 871)
  540 → 145 (→ 145)

  Starting with 69 produces a chain of five non-repeating terms, but the longest
  non-repeating chain with a starting number below one million is sixty terms.

  How many chains, with a starting number below one million, contain exactly 
  sixty non-repeating terms?

  Answer: 402 Completed on Thu, 4 Dec 2014, 10:33
  https://projecteuler.net/problem=74
  
  @author Botu Sun
'''

import math

factorials = [1] * 10
for i in xrange(1, 10):
  factorials[i] = factorials[i - 1] * i
print factorials

# loopers have predifined/cached value which minimize the calculation time.
loopers = {145: 0, 169: 2, 871: 1, 872: 1, 40585: 0} # 40585 is also a looper.

count = 0
for i in xrange(3, 1000000):
  chain = 1
  numbers = []
  breaked = False
  while i not in loopers:
    if i == 2: 
      breaked = True
      break
    numbers.append(i)
    total = 0
    while i:
      total += factorials[i % 10]
      i /= 10
    i = total
    chain += 1
  chain += loopers.get(i, 0)
  if breaked:
    continue
    
  if chain == 60:
    count += 1
  
  
  
print count
