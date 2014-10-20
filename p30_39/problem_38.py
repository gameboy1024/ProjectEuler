# -*- coding: utf-8 -*-
'''
  Pandigital multiples
  Problem 38
  
  Take the number 192 and multiply it by each of 1, 2, and 3:

  192 × 1 = 192
  192 × 2 = 384
  192 × 3 = 576
  By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

  The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

  What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
  
  Answer: 932718654 Completed on Mon, 20 Oct 2014, 22:08
  https://projecteuler.net/problem=38
  
  @author Botu Sun
'''

def IsPandigital(n):
  if len(str(n)) != 9:
    return False
  map = {'0': True}
  for c in str(n):
    if map.has_key(c):
      return False
    map[c] = True
  return True
  
max_pandigital = 0
for i in xrange(1, 9876):
  tmp = str(i)
  j = 2
  while(len(tmp) < 9):
    tmp += str(j * i)
    j += 1
  if IsPandigital(tmp):
    if int(tmp) > max_pandigital:
      print i, j
      max_pandigital = int(tmp)
      
print max_pandigital
      