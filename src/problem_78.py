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
'''
def Function(x, y, map):
  if x <= 1 or y <= 1:
    return 1
  if y > x and (x, x) in map:
    return map[(x, x)]
  if (x, y) in map:
    return map[(x, y)]
  sum = 0
  limit = x - y - 1 if x > y else -1
  for i in xrange(x - 1, limit, -1):
    sum += Function(i, x - i, map)
  map[(x, y)] = sum
  return sum

map = {}

i = 1
result = 1
while result % 10000 != 0 and i < 20:
  i += 1
  result = Function(i, i, map)
  print i, result, map
print i
'''
'''
import math

def P(n, map):
  if n < 0: return 0
  if n == 0: return 1
  sum = 0
  limit = (0.5 + math.sqrt(0.25 + 24 * n)) / 6
  for i in xrange(1, int(limit) + 1):
    sum += (-1) ** (i + 1) * (
        P(n - i * (3 * i - 1) / 2, map) + P(n - i * (3 * i + 1) / 2, map))
  # map[n] = sum
  return sum

map = {0: 0, 1: 1, 2: 2, 3: 3, 4: 5}
i = 5
result = 1
while(result % 10000 != 0):
  result = P(i, map)
  print i, result
  i += 1

print i
'''
def accelAsc(n):
    a = [0 for i in range(n + 1)]
    k = 1
    y = n - 1
    while k != 0:
        x = a[k - 1] + 1
        k -= 1
        while 2*x <= y:
            a[k] = x
            y -= x
            k += 1
        l = k + 1
        while x <= y:
            a[k] = x
            a[l] = y
            yield a[:k + 2]
            x += 1
            y -= 1
        a[k] = x + y
        y = x + y - 1
        yield a[:k + 1]

generator = accelAsc(100)

for i in generator:
  if len(i) == 1:
    print i
    exit()
  # raw_input()