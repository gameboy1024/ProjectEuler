# -*- coding: utf-8 -*-
'''
  Self powers
  Problem 48
  
  The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

  Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

  Answer: 9110846700 Completed on Wed, 22 Oct 2014, 00:00
  https://projecteuler.net/problem=48
  
  @author Botu Sun
'''

sum = 0
for i in xrange(1, 1001):
  tmp = 1
  for j in xrange(1, i + 1):
    tmp *= i
    tmp %= int(1E10)
    if tmp == 0:
      break
  sum += tmp
  sum %= int(1E10)
  
print sum