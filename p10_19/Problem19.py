'''
  Counting Sundays
  Problem 19
  
  You are given the following information, but you may prefer to do some research for yourself.

  1 Jan 1900 was a Monday.
  Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
  A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
  How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
  
  Answer: 171 Completed on Mon, 13 Oct 2014, 21:13
  https://projecteuler.net/problem=19
  
  @author Botu Sun
'''

day_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Use %7 to determine if it's Sunday. Monday then correspond to 1 + 7n.
date = 1
# The actual calculation starts with 1 Jan 1901. 1900 is not a leap year.
date += sum(day_in_month)

count = 0
for year in xrange(1901, 2001):
  if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    day_in_month[1] = 29
  else:
    day_in_month[1] = 28
  for month in xrange(0, 12):
    if date % 7 == 0:
      count += 1
    date += day_in_month[month]
    print date
    
print count