import math

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
  if reverse:
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

class PrimeChecker(object):
  '''A more advanced prime checker that uses elimination as base. Quicker.'''
  def __init__(self, limit):
    self._limit = int(limit)
    self._prime_map = {}
    self._prime_list = []
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
    # TODO: handle keyerror exception.
    if n > self._limit:
      return is_prime(n)
    else:
      return n in self._prime_map
    