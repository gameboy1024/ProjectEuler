# -*- coding: utf-8 -*-
'''
  Arithmetic expressions
  Problem 93
  By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and 
  making use of the four arithmetic operations (+, −, *, /) and 
  brackets/parentheses, it is possible to form different positive integer 
  targets.
  
  For example,
  
  8 = (4 * (1 + 3)) / 2
  14 = 4 * (3 + 1 / 2)
  19 = 4 * (2 + 3) − 1
  36 = 3 * 4 * (2 + 1)
  
  Note that concatenations of the digits, like 12 + 34, are not allowed.
  
  Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different 
  target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can
  be obtained before encountering the first non-expressible number.
  
  Find the set of four distinct digits, a < b < c < d, for which the longest set
  of consecutive positive integers, 1 to n, can be obtained, giving your answer 
  as a string: abcd.

  Answer: 1258 Completed on Sat, 18 Apr 2015, 12:07
  https://projecteuler.net/problem=93
  
  @author Botu Sun
'''

import itertools

# Errh! Didn't know there was a eval() so I wrote this...
# But OTOH eval miscalculate 2/3 as 0 while this handles it well.
def calculate_expression(exp):
  '''Calculate a infix expression.'''
  # Infix to postfix
  postfix = ''
  stack = []
  for c in exp:
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
      postfix += c
    elif c == '(':
      stack.append(c)
    elif c == ')':
      while len(stack) and stack[-1] != '(':
        postfix += stack.pop()
      if stack[-1] == '(':
        stack.pop()
    elif (not len(stack) or stack[-1] == '(' or 
        (c == '*' or c == '/') and (stack[-1] == '+' or stack[-1] == '-')):
        stack.append(c)
    else:
      while (len(stack) and stack[-1] != '(' and not(
        (c == '*' or c == '/') and (stack[-1] == '+' or stack[-1] == '-'))):
        postfix += stack.pop()
      stack.append(c)
  while len(stack):
    postfix += stack.pop()
  # print postfix
  # Calculate the value of postfix
  for c in postfix:
    if ord(c) >= ord('0') and ord(c) <= ord('9'):
      stack.append(ord(c) - ord('0'))
    else:
      y = stack.pop()
      x= stack.pop()
      if c == '+':
        stack.append(x + y)
      elif c == '-':
        stack.append(x - y)
      elif c == '*':
        stack.append(x * y)
      else:
        if y == 0:
          return -1
        stack.append(x * 1.0 / y)
  return stack.pop()

def digit_2_operator(i):
  if i == 0:
    return '+'
  elif i == 1:
    return '-'
  elif i == 2:
    return '*'
  else:
    return '/'

def calculate_consecutive_length(p, num_dict):
  global parentheses_pos
  i = 0
  while i < 4 ** 3:
    q = p[:]
    q.insert(1, digit_2_operator(i / 16))
    q.insert(3, digit_2_operator(i % 16 / 4))
    q.insert(5, digit_2_operator(i % 4))
    # print 'Operators added:', ''.join(p)
    for a, b in parentheses_pos:
      r = q[:]
      for k in a:
        r.insert(k, '(')
      for k in b:
        r.insert(k, ')')
      # print 'Parentheses added', ''.join(p)
      num_dict[calculate_expression(r)] = True
    i += 1


digits_set = [str(i) for i in xrange(1, 10)]
parenthesis_templates = []
parentheses_pos = (((0, 0), (5, 8)), ((0, 3), (7, 7)), ((2, 5), (9, 9)), 
  ((2, 2), (7, 10)), ((0, 5), (4, 10)))


max_length = 0
max_c = None
for c in itertools.combinations(digits_set, 4):
  print c
  num_dict = {}
  for p in itertools.permutations(c):
    calculate_consecutive_length(list(p), num_dict)
  i = 0
  while i in num_dict:
    i += 1
  if i - 1 > max_length:
    max_length = i - 1
    max_p = p
print max_length, sorted(max_p)