import math

################################################################################
# Basic operations
################################################################################

def is_even(n):
  return n % 2 == 0

def is_square(n):
  root = math.sqrt(n)
  return root == int(root)
  
def is_palindrome(n):
  '''Test if a number/str is a palindrome, like 12321.'''
  s = str(n)
  length = len(s)
  for i in xrange(0, length / 2):
    if s[i] != s[length - i - 1]:
      return False
  return True

def reverse_str(s):
  return s[::-1]
  
def reverse_number(n):
  # Leading zeros are handled correctly by native casting.
  if type(n) == int:
    return int(reverse_str(str(n)))
  elif type(n) == long:
    return long(reverse_str(str(n)))
    
def gcd(a, b):
  while b:
    tmp = b
    b = a % b
    a = tmp
  return a

################################################################################
# Large number operations
################################################################################

UNIT_LENGTH = 9

def add(a, b):
  a = str(a)[::-1]
  b = str(b)[::-1]
  result = ''
  i = 0
  carry = 0
  while carry != 0 or i < max(len(a), len(b)):
    sum = carry
    if i < len(a):
      # ord('0') = 48
      sum += ord(a[i]) - 48
    if i < len(b):
      sum += ord(b[i]) - 48
    carry = sum / 10
    result += str(sum % 10)
    i += 1
  return result[::-1]
  

def mul(a, b):
  '''
  Calculate the multiplication of two large int.

  Args:
    a: a list of int, representing digits of a large int. The digits are 
      reversed so 123 is [3, 2, 1]
    b: same as a

  Return:
    Reversed list of digits of the multiplication.
  '''
  pass

def power_list(a, b, reverse=False):
  result = [1]
  for i in xrange(0, b):
    carry = 0
    j = 0
    while carry != 0 or len(result) > j:
      if j == len(result):
        result.append(0)
      result[j]  = result[j] * a + carry
      
      carry = result[j] / 10
      result[j] %= 10
      # print carry
      j += 1
  if not reverse:
    result = result[::-1]
  return result
  
################################################################################
# Prime related utils
################################################################################

def is_prime(n):
  '''Naive way of prime checking, only use for occasional checks.'''
  if n < 2: return False
  if n == 2: return True
  for i in xrange(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def totient(n, factors):
  result = n
  for f in factors:
    n *= 1 - 1.0 / f
  return int(n)
  
class PrimeChecker(object):
  '''A more advanced prime checker that uses seive.'''
  def __init__(self, limit):
    self._limit = int(limit)
    self._prime_map = {}
    self._prime_list = []
    self.seive()
    
  def seive(self):
    numbers = [True] * (self._limit + 1)
    for i in xrange(2, self._limit / 2 + 1):
      if numbers[i] == True:
        j = i * 2
        while (j <= self._limit):
          numbers[j] = False
          j += i
    for i in xrange(2, self._limit + 1):
      if numbers[i] == True:
        self._prime_map[i] = True
        self._prime_list.append(i)
  
  def get_prime_map(self):
    return self._prime_map
    
  def get_prime_list(self):
    return self._prime_list
  
  def is_prime(self, n):
    if n > self._limit:
      return is_prime(n)
    else:
      return n in self._prime_map

class PrimeFactorsGenerator(PrimeChecker):
  '''A prime factors generator'''
  def seive(self):
    self._prime_factor = []
    for i in xrange(0, self._limit + 1):
      self._prime_factor.append([])
    numbers = [True] * (self._limit + 1)
    for i in xrange(2, self._limit / 2 + 1):
      if numbers[i] == True:
        self._prime_factor[i].append(i)
        j = i * 2
        while (j <= self._limit):
          numbers[j] = False
          self._prime_factor[j].append(i)
          j += i
    # The upper part from limit/2 to limit is not calculated yet.
    for i in xrange(self._limit / 2 + 1, self._limit + 1):
      if not len(self._prime_factor[i]):
        self._prime_factor[i].append(i)
    
    for i in xrange(2, self._limit + 1):
      if numbers[i] == True:
        self._prime_map[i] = True
        self._prime_list.append(i)
  
  def get_prime_factors(self):
    return self._prime_factor
