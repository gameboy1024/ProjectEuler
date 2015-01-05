# -*- coding: utf-8 -*-
'''
  Singular integer right triangles
  Problem 75
  
  It turns out that 12 cm is the smallest length of wire that can be bent to 
  form an integer sided right angle triangle in exactly one way, but there are 
  many more examples.

  12 cm: (3,4,5)
  24 cm: (6,8,10)
  30 cm: (5,12,13)
  36 cm: (9,12,15)
  40 cm: (8,15,17)
  48 cm: (12,16,20)

  In contrast, some lengths of wire, like 20 cm, cannot be bent to form an 
  integer sided right angle triangle, and other lengths allow more than one 
  solution to be found; for example, using 120 cm it is possible to form exactly
  three different integer sided right angle triangles.

  120 cm: (30,40,50), (20,48,52), (24,45,51)

  Given that L is the length of the wire, for how many values of L ≤ 1,500,000 
  can exactly one integer sided right angle triangle be formed?

  Answer: 161667 Completed on Mon, 5 Jan 2015, 23:47
  https://projecteuler.net/problem=75
  
  @author Botu Sun
'''

LIMIT = 1500000

triples = [(3, 4, 5)]
current = 0
newed = True
while newed or current < len(triples):
  a, b, c = triples[current]
  newed = False
  aa = a - 2 * b + 2 * c
  bb = 2 * a - b + 2 * c
  cc = 2 * a - 2 * b + 3 * c
  if aa + bb + cc <= LIMIT:
    triples.append((aa, bb, cc))
    newed = True
  aa = a + 2 * b + 2 * c
  bb = 2 * a + b + 2 * c
  cc = 2 * a + 2 * b + 3 * c
  if aa + bb + cc <= LIMIT:
    triples.append((aa, bb, cc))
    newed = True
  aa = - a + 2 * b + 2 * c
  bb = -2 * a + b + 2 * c
  cc = -2 * a + 2 * b + 3 * c
  if aa + bb + cc <= LIMIT:
    triples.append((aa, bb, cc))
    newed = True
  current += 1
  
print "triples finished!", len(triples)

map = {}
for t in triples:
  s = sum(t)
  x = 1
  while s * x <= LIMIT:
    map[s * x] = map.get(s * x, 0) + 1
    x += 1
print "map constructed", len(map)

count = 0
for v in map.values():
  if v == 1:
    count += 1
print count