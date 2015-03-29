# -*- coding: utf-8 -*-
'''
  Cuboid route
  Problem 86
  
  A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a
  fly, F, sits in the opposite corner. By travelling on the surfaces of the room
  the shortest "straight line" distance from S to F is 10 and the path is shown 
  on the diagram.


  However, there are up to three "shortest" path candidates for any given cuboid
  and the shortest route doesn't always have integer length.

  It can be shown that there are exactly 2060 distinct cuboids, ignoring 
  rotations, with integer dimensions, up to a maximum size of M by M by M, for 
  which the shortest route has integer length when M = 100. This is the least 
  value of M for which the number of solutions first exceeds two thousand; the 
  number of solutions when M = 99 is 1975.

  Find the least value of M such that the number of solutions first exceeds one 
  million.

  Answer:
  https://projecteuler.net/problem=86
  
  @author Botu Sun
'''
import math

def generate_triples(m):
  # First generate all rec triangles triples.
  triples = [(3, 4, 5)]
  current = 0
  newed = True
  while newed or current < len(triples):
    a, b, c = triples[current]
    newed = False
    aa = a - 2 * b + 2 * c
    bb = 2 * a - b + 2 * c
    cc = 2 * a - 2 * b + 3 * c
    aaa = aa
    bbb = bb
    ccc = cc
    while max(aaa, bbb) <= 2 * m and min(aaa, bbb) <= m:
      triples.append((aaa, bbb, ccc))
      aaa += aa
      bbb += bb
      ccc += cc
      newed = True
    aa = a + 2 * b + 2 * c
    bb = 2 * a + b + 2 * c
    cc = 2 * a + 2 * b + 3 * c
    aaa = aa
    bbb = bb
    ccc = cc
    while max(aaa, bbb) <= 2 * m and min(aaa, bbb) <= m:
      triples.append((aaa, bbb, ccc))
      aaa += aa
      bbb += bb
      ccc += cc
      newed = True
    aa = - a + 2 * b + 2 * c
    bb = -2 * a + b + 2 * c
    cc = -2 * a + 2 * b + 3 * c
    aaa = aa
    bbb = bb
    ccc = cc
    while max(aaa, bbb) <= 2 * m and min(aaa, bbb) <= m:
      triples.append((aaa, bbb, ccc))
      aaa += aa
      bbb += bb
      ccc += cc
      newed = True
    current += 1
  return triples

def get_possible_combinations(a, b, c, m, solutions):
  modified = False
  if b <= m:
    for i in xrange(1, int(a / 2) + 1):
      solutions[tuple(sorted([i, a - i, b]))] = True
      modified = True
    for i in xrange(b - a, int(b / 2) + 1):
      if i <= a and b - i <= a:
        solutions[tuple(sorted([a, i, b - i]))] = True
        modified = True
  elif a <= m and b <= m * 2:
    for i in xrange(b - m, int(b / 2) + 1):
      if i <= a and b - i <= a:
        solutions[tuple(sorted([a, i, b - i]))] = True
        modified = True
  return modified

def get_num_solutions(m, target):
  triples = generate_triples(m)
  solutions = {}
  for triple in triples:
    triple = sorted(triple)
    a, b, c = triple
    while get_possible_combinations(a, b, c, m, solutions):
      a += triple[0]
      b += triple[1]
      c += triple[2]
  print m, len(solutions)
  if len(solutions) > target:
    print m
    exit()

i = 4000
while True:
  get_num_solutions(i, 1000000)
  i += 1