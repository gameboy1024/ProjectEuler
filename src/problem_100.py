# -*- coding: utf-8 -*-
'''
  Arranged probability
  Problem 100
  
  If a box contains twenty-one coloured discs, composed of fifteen blue discs 
  and six red discs, and two discs were taken at random, it can be seen that the
  probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
  
  The next such arrangement, for which there is exactly 50% chance of taking two
  blue discs at random, is a box containing eighty-five blue discs and 
  thirty-five red discs.
  
  By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 
  discs in total, determine the number of blue discs that the box would contain.
  
  https://projecteuler.net/problem=100
  
  @author Botu Sun
'''
################################################################################
# Following is the first bruteforce attempt. While it doesn't work beyond 
# 27304197. It still showed that there is a pattern between the ratio between
# 2 consecutive arrangements. This helps build the second solution.
################################################################################
# import math
# def root_of_target_i(n):
#   return (2 + math.sqrt(4 + 8 * n * (n - 1))) / 4
# precedent_total = 21
# precedent_b = 15
# n = int(1E1)
# while precedent_total < 1E12:
#   root = int(root_of_target_i(n))
#   for i in xrange(int(root) - 1, int(root) + 1):
#     if n * (n - 1) == 2 * i * (i - 1):
#       precedent = n
#       precedent_b = i
#       print n, i, n - i, i * 1.0 / n, (n - i) * 1.0 / i
#       n = n * 5
#       continue
#   n += 1
# print precedent_total, precedent_b

################################################################################
# This is the second step, the solution.
################################################################################
import math

# We easily know that the number of blues is roughly sqrt(2)/2 of the total.
half_sqrt2 = 0.7071067811865476

limit = 10 ** 12
last_total = 21
last_blue = 15
last_ratio = 5
next_total = last_total * last_ratio
while True:
  next_blue = int(next_total * half_sqrt2) + 1
  if 2 * next_blue * next_blue - 2 * next_blue == next_total * next_total - next_total:
    print '%s discs in total, %s of blue and %s of red!' % (next_total, next_blue, next_total - next_blue)
    last_ratio = next_total * 1.0 / last_total
    last_total = next_total
    last_blue = next_blue
    next_total = int(last_total * last_ratio)
    if last_total > 1E12:
      break
  else:
    next_total += 1

  