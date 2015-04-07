# -*- coding: utf-8 -*-
'''
  Product-sum numbers
  Problem 88
  A natural number, N, that can be written as the sum and product of a given set
  of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum 
  number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
  
  For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
  
  For a given set of size, k, we shall call the smallest N with this property a 
  minimal product-sum number. The minimal product-sum numbers for sets of size, 
  k = 2, 3, 4, 5, and 6 are as follows.
  
  k=2: 4 = 2 × 2 = 2 + 2
  k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
  k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
  k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
  k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
  
  Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 
  30; note that 8 is only counted once in the sum.
  
  In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 
  6, 8, 12, 15, 16}, the sum is 61.
  
  What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

  
  https://projecteuler.net/problem=88
  
  @author Botu Sun
'''

'''
  Idea: The multiplication is small than the sum until it isn't. So we are going
  to increment number by number until when multiplication is bigger or equality 
  is found. E.g. 1 X 2 X 2?1 + 2 + 2, then 123,124,125...133,134,135...144..
'''

################################################################################
# This one is too difficult for me, I came up with an idea but was too slow. 
# I then found this solution on the internet which is brilliant. A clear
# explanation can be found on the forum of the question.

def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]: n[k] = p
        for i in range(start, kmax//p * 2):
            prodsum(p*i, s+i, c+1, i)

kmax = 12000
n = [2*kmax] * kmax    # the minimal product-sum is < 2*k + 1 
prodsum(1, 1, 1, 2)

#  convert to set to remove duplicates from slice of n
print "Project Euler 88 Solution =", sum(set(n[2:]))
exit()

################################################################################
# Here's my code
import sys

def get_product_and_sum(a):
  '''Compare the multiplication and the sum of a list of numbers.'''
  sum_result = len(a)
  prod_result = 1
  i = 0
  while i < len(a) and a[i] != 1:
    sum_result += a[i] - 1
    prod_result *= a[i]
    i += 1
  return prod_result, sum_result
  
def compare(a):
  prod_result, sum_result = get_product_and_sum(a)
  return prod_result - sum_result
  
def increment(a, k, min_number):
  '''Increment a number, a as a list, k as the value for k.'''
  # Test if it's a product-sum number
  prod_result, sum_result = get_product_and_sum(a)
  if prod_result == sum_result:
    # print "Found: ", sum(a)
    if sum_result < min_number[0]:
      min_number[0] = sum_result
  # Increment
  n = 0
  a[n] += 1
  # If product > sum, we carry over
  while compare(a) > 0:
    if n == k - 1:
      return False
    n += 1
    a[n] += 1
    for i in xrange(0, n):
      a[i] = a[n]
  # print n, a
  return True
  
LIMIT = 12000
product_sum_numbers = {}
for k in xrange(2, LIMIT + 1):
  print k
  a = [2, 2] + [1] * (k - 2)
  min_number = [sys.maxint]
  while increment(a, k, min_number):
    pass
  product_sum_numbers[min_number[0]] = True
  # print a
  
print product_sum_numbers.keys()
print sum(product_sum_numbers.keys())
