'''
  Lexicographic permutations
  Problem 24
  
  A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

  012   021   102   120   201   210

  What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
  
  Answer: 2783915460 Completed on Tue, 14 Oct 2014, 18:28
  https://projecteuler.net/problem=24
  
  @author Botu Sun
'''

count = 0

def Recursion(a, n):
  global count
  if n == 10:
    count += 1
    if count == 1E6:
      for i in xrange(0, 10):
        a[i] = str(a[i])
      print ''.join(a)
      exit()
    return
  for i in xrange(0, 10):
    if i not in a:
      a.append(i)
      Recursion(a, n + 1)
      a.pop()

a = []

Recursion(a, 0)