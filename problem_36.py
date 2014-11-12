# -*- coding: utf-8 -*-
'''
  Double-base palindromes
  Problem 36
  
  The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

  Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

  (Please note that the palindromic number, in either base, may not include leading zeros.)
  
  Answer: 872187 Completed on Thu, 16 Oct 2014, 22:05
  https://projecteuler.net/problem=36
  
  @author Botu Sun
'''

def IsPalindromic(s):
  length = len(s)
  for i in xrange(0, length / 2):
    if s[i] != s[length - i - 1]:
      return False
  return True

sum = 0
for i in xrange(1, int(1E6)):
  if IsPalindromic(str(i)) and IsPalindromic(bin(i)[2:]):
    sum += i
    
print sum