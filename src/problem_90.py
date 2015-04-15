# -*- coding: utf-8 -*-
'''
  Cube digit pairs
  Problem 90
  
  Each of the six faces on a cube has a different digit (0 to 9) written on it; 
  the same is done to a second cube. By placing the two cubes side-by-side in 
  different positions we can form a variety of 2-digit numbers.
  
  For example, the square number 64 could be formed:
  
  
  In fact, by carefully choosing the digits on both cubes it is possible to 
  display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 
  49, 64, and 81.
  
  For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on 
  one cube and {1, 2, 3, 4, 8, 9} on the other cube.
  
  However, for this problem we shall allow the 6 or 9 to be turned upside-down 
  so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows 
  for all nine square numbers to be displayed; otherwise it would be impossible 
  to obtain 09.
  
  In determining a distinct arrangement we are interested in the digits on each 
  cube, not the order.
  
  {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
  {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
  
  But because we are allowing 6 and 9 to be reversed, the two distinct sets in 
  the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
  purpose of forming 2-digit numbers.
  
  How many distinct arrangements of the two cubes allow for all of the square 
  numbers to be displayed?

  Answer: 1217 Completed on Wed, 15 Apr 2015, 14:02
  https://projecteuler.net/problem=90
  
  @author Botu Sun
'''
'''
  Tried to do this with my own way: use bit operation to get all the possible
  allocations of pairs of the squares and fill up remaining slots with all
  numbers. But I never got clear with the description of unique combination so
  the result is incorrect(handling 6 and 9). Here's the code though:
'''
def recursive_fill_a(a, b, pairs):
  '''Recursively add element to fill up all faces.'''
  if len(a) == 7 or len(a) == 6:
    recursive_fill_b(a, b, pairs)
    if len(a) != 6:
      return
  for i in xrange(0, 9):
    if str(i) in a:
      continue
    a[str(i)] = True
    if i == 6: a['9'] = True
    recursive_fill_a(a, b, pairs)
    a.pop(str(i))
    if i == 6: a.pop('9')
    
def recursive_fill_b(a, b, pairs):
  if len(b) == 7 or len(b) == 6:
    add_to_all_pairs(a, b, pairs)
    if len(b) != 6:
      return
  for i in xrange(0, 9):
    if str(i) in b:
      continue
    b[str(i)] = True
    if i == 6: b['9'] = True
    recursive_fill_b(a, b, pairs)
    b.pop(str(i))
    if i == 6: b.pop('9')

def add_to_all_pairs(a, b, all_pairs):
  a_str = ''.join(sorted(a.keys()))
  b_str = ''.join(sorted(b.keys()))
  all_pairs[
    a_str + '_' + b_str if a_str < b_str else b_str + '_' + a_str] = True
    
squares = [('0', '1'), ('0', '4'), ('0', '9'), ('1', '6'), ('2', '5'), 
  ('3', '6'), ('4', '9'), ('6', '4'), ('8', '1')]

limit = 2 ** 9
all_pairs = {}
for i in xrange(0, limit):
  a = {}
  b = {}
  for j in xrange(0, 9):
    # Use bit operation to cover all the possible combinations
    if i >> j & 1:
      a[squares[j][0]] = True
      b[squares[j][1]] = True
    else:
      a[squares[j][1]] = True
      b[squares[j][0]] = True
  if '6' in a: a['9'] = True
  if '9' in a: a['6'] = True
  if '6' in b: b['9'] = True
  if '9' in b: b['6'] = True
  if len(a) > 7 or ('6' not in a and len(a) == 7):
    continue
  if len(b) > 7 or ('6' not in b and len(b) == 7):
    continue
  recursive_fill_a(a, b, all_pairs)
  
print len(all_pairs)

'''
  And correct code from the internet (brute-force):
'''
from itertools import combinations

squares = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)]
cube = list(combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 6], 6))

def valid(c1, c2):
    return all(x in c1 and y in c2 or x in c2 and y in c1 for x, y in squares)

print sum(1 for i, c1 in enumerate(cube) for c2 in cube[:i] if valid(c1, c2))