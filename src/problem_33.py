# -*- coding: utf-8 -*-
'''
  Digit canceling fractions
  Problem 33
  
  The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

  We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

  There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

  If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
  
  Answer: 100 Completed on Wed, 15 Oct 2014, 23:42
  https://projecteuler.net/problem=33
  
  @author Botu Sun
'''

import math

mul_a = 1
mul_b = 1
for b in xrange(10, 100):
  for a in xrange(10, b):
    for i in xrange(1, 10):
      if str(i) in str(a) and str(i) in str(b):
        a_l = [c for c in str(a)]
        b_l = [c for c in str(b)]
        a_l.remove(str(i))
        b_l.remove(str(i))
        if b_l[0] != '0' and abs(float(a) / b - float(''.join(a_l)) / float(''.join(b_l))) < 1E-6:
          mul_a *= a
          mul_b *= b

for i in xrange(mul_a, 1, -1):
  if mul_a % i == 0 and mul_b % i == 0:
    print mul_b / i
    exit()