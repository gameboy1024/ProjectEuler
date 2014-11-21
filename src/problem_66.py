# -*- coding: utf-8 -*-
'''
  Diophantine equation
  Problem 66
  Consider quadratic Diophantine equations of the form:

  x2 – Dy2 = 1

  For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

  It can be assumed that there are no solutions in positive integers when D is 
  square.

  By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the 
  following:

  32 – 2×22 = 1
  22 – 3×12 = 1
  92 – 5×42 = 1
  52 – 6×22 = 1
  82 – 7×32 = 1

  Hence, by considering minimal solutions in x for D ≤ 7, the largest x is 
  obtained when D=5.

  Find the value of D ≤ 1000 in minimal solutions of x for which the largest 
  value of x is obtained.

  Answer: 661 Completed on Fri, 21 Nov 2014, 14:39
  https://projecteuler.net/problem=66
  
  @author Botu Sun
'''

import math
from lib import math_utils

def valid_xy(d, x, y):
  return x * x == d * y * y + 1

# http://en.wikipedia.org/wiki/Pell's_equation
class ContinuedFractions(object):
  
  def __init__(self, n):
    self._n = n
    self._root, self._sequence = self.get_period(n)
    self._period = len(self._sequence)
    
  def get_period(self, n):
    # The idea comes from:
    # http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#section7
    numbers = []
    first_root = None
    c = 0
    d = 1
    while True:
      nearest_root = int((math.sqrt(n) + c) / d)
      if not first_root:
        first_root = nearest_root
      else:
        numbers.append(nearest_root)
      c -=  nearest_root * d  
      d = (n - c * c) / d
      c = -c
      if d == 1:
        numbers.append(int(math.sqrt(n) + c))
        return first_root, numbers
  
  def get_a(self, n):
    if n == 0:
      return self._root
    return self._sequence[(n - 1) % self._period]
  
  def get_convergent(self, current, n):
    if current == n:
      return self.get_a(n), 1
    denom, nom = self.get_convergent(current + 1, n)
    nom += denom * self.get_a(current)
    return nom, denom
  
  def get_xy(self):
    denom = 1
    nom = self._root
    i = 1
    while not valid_xy(self._n, nom, denom):
      nom, denom = self.get_convergent(0, i)
      i += 1
    return nom, denom
    
max = 0
max_d = 0

for i in xrange(2, 1001):
  if math.pow(int(math.sqrt(i)), 2) == i:
    continue
  number = ContinuedFractions(i)
  x, y = number.get_xy()
  if x > max:
    max = x
    max_d = i
    
print max_d
