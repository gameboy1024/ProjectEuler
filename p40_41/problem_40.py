# -*- coding: utf-8 -*-
'''
  Champernowne's constant
  Problem 40
  
  An irrational decimal fraction is created by concatenating the positive 
  integers:

  0.123456789101112131415161718192021...

  It can be seen that the 12th digit of the fractional part is 1.

  If dn represents the nth digit of the fractional part, find the value of the 
  following expression.

  d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
  
  Answer: 210 Completed on Mon, 20 Oct 2014, 23:02
  https://projecteuler.net/problem=40
  
  @author Botu Sun
'''

import math

def GetDigit(n):
  '''Get the n-th digit of the Champernowne's constant.

  First, there're 9 1-digit numbers, 1-9, 90 2-digit numbers, 10-99, 900 3-digit
  numbers, 100-999, etc. We first calculate the n-th digit fells in which 
  interval, IOW the number containing n-th digit has how many digits. Then we 
  get the number, finally the digit.
  '''
  count = 0
  digits_per_number = 1
  # The number of digits for all the n-digit numbers. 1-9: 9; 10-99: 180; 
  # 100-999: 2700
  next_number_set = 9
  while (count + next_number_set <= n):
    count += next_number_set
    digits_per_number += 1
    next_number_set = digits_per_number * int(
        math.pow(10, digits_per_number - 1)) * 9
  return int(str(int(math.ceil(float(n - count) / digits_per_number)) + int(
      math.pow(10, digits_per_number - 1) - 1))[
          (n - count) % digits_per_number - 1])

result = 1
result *= GetDigit(1)
result *= GetDigit(10)
result *= GetDigit(100)
result *= GetDigit(1000)
result *= GetDigit(10000)
result *= GetDigit(100000)
result *= GetDigit(1000000)
print result