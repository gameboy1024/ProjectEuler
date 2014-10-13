'''
  If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

  If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


  NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
  
  Answer: 21124 Completed on Mon, 13 Oct 2014, 19:39
  https://projecteuler.net/problem=17
  
  @author Botu Sun
'''

letter_count = {0: 0,
                1: 3,
                2: 3,
                3: 5,
                4: 4,
                5: 4,
                6: 3,
                7: 5,
                8: 5,
                9: 4,
                10: 3,
                11: 6,
                12: 6,
                13: 8,
                14: 8,
                15: 7,
                16: 7,
                17: 9,
                18: 8,
                19: 8,
                20: 6,
                30: 6,
                40: 5,
                50: 5,
                60: 5,
                70: 7,
                80: 6,
                90: 6,
                100: 7,
                1000: 8}

def GetLetterCount(i):
  if i == 1000:
    return letter_count[1] + letter_count[1000]
  elif i >= 100:
    return letter_count[i / 100] + letter_count[100] + ((GetLetterCount(i % 100) + 3) if i % 100 != 0 else 0)
  elif i >= 20:
    return letter_count[i - i % 10] + letter_count[i % 10]
  else:
    return letter_count[i]

sum = 0
for i in xrange(1, 1001):
  sum += GetLetterCount(i)
print sum