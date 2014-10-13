# -*- coding: utf-8 -*-
'''
  Factorial digit sum
  Problem 20
  
  n! means n * (n − 1) * ... * 3 * 2 * 1

  For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
  and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

  Find the sum of the digits in the number 100!
  
  Answer: 648 Completed on Mon, 13 Oct 2014, 21:48
  https://projecteuler.net/problem=20
  
  @author Botu Sun
'''

buf = [0] * 200
buf[0] = 1
len = 1
for i in xrange(2, 101):
  carry = 0
  k = 0
  while(carry != 0 or k < len):
    tmp = buf[k] * i + carry
    buf[k] = tmp % 10
    carry = tmp / 10
    k += 1
  len = k
  
print sum(buf)