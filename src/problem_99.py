# -*- coding: utf-8 -*-
'''
  Largest exponential
  Problem 99
  
  Comparing two numbers written in index form like 211 and 37 is not difficult, 
  as any calculator would confirm that 211 = 2048 < 37 = 2187.
  
  However, confirming that 632382518061 > 519432525806 would be much more 
  difficult, as both numbers contain over three million digits.
  
  Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
  containing one thousand lines with a base/exponent pair on each line, 
  determine which line number has the greatest numerical value.
  
  NOTE: The first two lines in the file represent the numbers in the example 
  given above.
  
  Answer: 709 Completed on Thu, 30 Apr 2015, 15:22
  https://projecteuler.net/problem=99
  
  @author Botu Sun
'''
from math import log10

pairs = []
with open('../res/p099_base_exp.txt', 'r') as f:
  line = f.readline()
  i = 1
  while line:
    x, y = line.split(',')
    pairs.append((int(x), int(y), i))
    line = f.readline()
    i += 1
print sorted(pairs, key=lambda (x, y, i): -log10(x) * y)[0][2]
