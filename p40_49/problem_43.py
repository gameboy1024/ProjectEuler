# -*- coding: utf-8 -*-
'''
  Sub-string divisibility
  Problem 43
  
  The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

  Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

  d2d3d4=406 is divisible by 2
  d3d4d5=063 is divisible by 3
  d4d5d6=635 is divisible by 5
  d5d6d7=357 is divisible by 7
  d6d7d8=572 is divisible by 11
  d7d8d9=728 is divisible by 13
  d8d9d10=289 is divisible by 17
  Find the sum of all 0 to 9 pandigital numbers with this property.

  Answer: 16695334890 Completed on Tue, 21 Oct 2014, 00:21
  https://projecteuler.net/problem=43
  
  @author Botu Sun
'''

def ValidNumber(n):
  return (len(str(n)) == 10 and
          int(str(n)[1:4]) % 2 == 0 and
          int(str(n)[2:5]) % 3 == 0 and
          int(str(n)[3:6]) % 5 == 0 and
          int(str(n)[4:7]) % 7 == 0 and
          int(str(n)[5:8]) % 11 == 0 and
          int(str(n)[6:9]) % 13 == 0 and
          int(str(n)[7:]) % 17 == 0)
         
def Recursion(a, current, n, total):
  global sum
  if n == total:
    if ValidNumber(current):
      print current
      sum += current
    return
  for i in xrange(0, total):
    if a[i] == False:
      tmp = current
      a[i] = True
      tmp *= 10
      tmp += total - 1 - i
      Recursion(a, tmp, n + 1, total)
      a[i] = False
      
sum = 0
a = [False] * 10
Recursion(a, 0, 0, 10)
print sum