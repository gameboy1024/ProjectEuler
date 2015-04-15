# -*- coding: utf-8 -*-
'''
  Square digit chains
  Problem 92
  
  A number chain is created by continuously adding the square of the digits in a
  number to form a new number until it has been seen before.
  
  For example,
  
  44 → 32 → 13 → 10 → 1 → 1
  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
  
  Therefore any chain that arrives at 1 or 89 will become stuck in an endless 
  loop. What is most amazing is that EVERY starting number will eventually 
  arrive at 1 or 89.
  
  How many starting numbers below ten million will arrive at 89?

  Answer: 8581146 Completed on Wed, 15 Apr 2015, 17:05
  https://projecteuler.net/problem=92
  
  @author Botu Sun
'''
def compute(n):
  tmp = 0
  while n != 0:
    tmp += (n % 10) ** 2
    n /= 10
  return tmp

# Construct 2 dicts of all possible numbers after first step (only 9^2 * 6)
dict_89 = {1: 0, 89: 1}
for i in xrange(1, 9 ** 2 * 7 + 1):
  result = i
  l = [result]
  while result not in dict_89:
    l.append(result)
    result = compute(result)
  for n in l:
    dict_89[n] = dict_89[result]
    
# Further optimization can be done by save ordered permunations to avoid 
# computing 123456, 654321 twice.
print (sum(dict_89.values()) + 
  sum([dict_89[compute(i)] for i in xrange(9 ** 2 * 7 + 1, int(1E7))]))
