# -*- coding: utf-8 -*-
'''
  1000-digit Fibonacci number
  Problem 25
  The Fibonacci sequence is defined by the recurrence relation:

  Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
  Hence the first 12 terms will be:

  F1 = 1
  F2 = 1
  F3 = 2
  F4 = 3
  F5 = 5
  F6 = 8
  F7 = 13
  F8 = 21
  F9 = 34
  F10 = 55
  F11 = 89
  F12 = 144
  The 12th term, F12, is the first term to contain three digits.

  What is the first term in the Fibonacci sequence to contain 1000 digits?
  
  Answer: 4782 Completed on Tue, 14 Oct 2014, 18:32
  https://projecteuler.net/problem=25
  
  @author Botu Sun
'''

def add(a, b, result):
  carry = 0
  for i in xrange(0, 1000):
    tmp = a[i] + b[i] + carry
    result[i] = tmp % 10
    carry = tmp / 10

a = [0] * 1000
b = [0] * 1000
a[0] = 1
b[0] = 1
count = 2
while b[999] == 0:
  add(a, b, a)
  tmp = b
  b = a
  a = tmp
  count += 1
  
print count