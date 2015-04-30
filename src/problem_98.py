# -*- coding: utf-8 -*-
'''
  Anagramic squares
  Problem 98
  By replacing each of the letters in the word CARE with 1, 2, 9, and 6 
  respectively, we form a square number: 1296 = 362. What is remarkable is that,
  by using the same digital substitutions, the anagram, RACE, also forms a 
  square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word
  pair and specify further that leading zeroes are not permitted, neither may a 
  different letter have the same digital value as another letter.
  
  Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
  containing nearly two-thousand common English words, find all the square 
  anagram word pairs (a palindromic word is NOT considered to be an anagram of 
  itself).
  
  What is the largest square number formed by any member of such a pair?
  
  NOTE: All anagrams formed must be contained in the given text file.
  
  Answer: 18769 Completed on Thu, 30 Apr 2015, 14:39
  https://projecteuler.net/problem=98
  
  @author Botu Sun
'''

from lib.math_utils import is_square
from itertools import permutations

f = open('../res/p098_words.txt', 'r')

words = [w[1:-1] for w in f.readline().split(',')]
anagrams_dict = {}
for w in words:
  sorted_w = ''.join(sorted(w))
  if sorted_w not in anagrams_dict:
    anagrams_dict[sorted_w] = []
  anagrams_dict[sorted_w].append(w)

for k, v in anagrams_dict.items():
  if len(v) == 1:
    anagrams_dict.pop(k)
  
print 'Dict done!'

def word_2_number(l2d, word):
  result = 0
  for l in word:
    result = result * 10 + l2d[l]
  return result

def find_squares(key, words):
  squares = []
  for p in permutations(range(0, 10), len(key)):
    l2d = {} # dict: letter -> digit
    for i in xrange(0, len(p)):
      l2d[key[i]] = p[i]
    # There's no triples, only pairs so using 0, 1 can be easier.
    # Test for starting 0s.
    if l2d[words[0][0]] == 0 or l2d[words[1][0]] == 0:
      continue
    number_1 = word_2_number(l2d, words[0])
    number_2 = word_2_number(l2d, words[1])
    if is_square(number_1) and is_square(number_2):
      squares.append(number_1)
      squares.append(number_2)
  return squares
  
max_square = -1
for k, v in sorted(anagrams_dict.items(), key=lambda (x, y): -len(x)):
  if len(str(k)) < len(str(max_square)):
    break
  squares = find_squares(k, v)
  for sq in squares:
    if sq > max_square:
      max_square = sq
print max_square