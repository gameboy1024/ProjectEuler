# -*- coding: utf-8 -*-
'''
  Triangular, pentagonal, and hexagonal
  Problem 45
  
  Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

  Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
  Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
  Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
  It can be verified that T285 = P165 = H143 = 40755.

  Find the next triangle number that is also pentagonal and hexagonal.

  Answer: 1533776805 Completed on Tue, 21 Oct 2014, 22:38
  https://projecteuler.net/problem=45
  
  @author Botu Sun
'''

def TriangleNumber(n):
  return n * (n + 1) / 2
  
def PentagonalNumber(n):
  return n * (3 * n - 1) / 2
  
def HexagonalNumber(n):
  return n * (2 * n - 1)

# Triangle number increment the slowest.  
i = 285 + 1
j = 165
k = 143

while(True):
  t = TriangleNumber(i)
  p = PentagonalNumber(j)
  h = HexagonalNumber(k)
  if t == p and p == h:
    print t
    exit(0)
  if t <= p and t <= h:
    i += 1
  elif p <= t and p <= h:
    j += 1
  else:
    k += 1