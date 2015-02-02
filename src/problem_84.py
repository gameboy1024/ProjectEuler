# -*- coding: utf-8 -*-
'''
  Monopoly odds
  Problem 84
  In the game, Monopoly, the standard board is set up in the following way:

  GO  A1  CC1 A2  T1  R1  B1  CH1 B2  B3  JAIL
  H2                                      C1
  T2                                      U1
  H1                                      C2
  CH3                                     C3
  R4                                      R2
  G3                                      D1
  CC3                                     CC2
  G2                                      D2
  G1                                      D3
  G2J F3  U2  F2  F1  R3  E3  E2  CH2 E1  FP

  A player starts on the GO square and adds the scores on two 6-sided dice to 
  determine the number of squares they advance in a clockwise direction. Without
  any further rules we would expect to visit each square with equal probability:
  2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH 
  (chance) changes this distribution.

  In addition to G2J, and one card from each of CC and CH, that orders the 
  player to go directly to jail, if a player rolls three consecutive doubles, 
  they do not advance the result of their 3rd roll. Instead they proceed 
  directly to jail.

  At the beginning of the game, the CC and CH cards are shuffled. When a player 
  lands on CC or CH they take a card from the top of the respective pile and, 
  after following the instructions, it is returned to the bottom of the pile. 
  There are sixteen cards in each pile, but for the purpose of this problem we 
  are only concerned with cards that order a movement; any instruction not 
  concerned with movement will be ignored and the player will remain on the 
  CC/CH square.

  Community Chest (2/16 cards):
  Advance to GO
  Go to JAIL

  Chance (10/16 cards):
  Advance to GO
  Go to JAIL
  Go to C1
  Go to E3
  Go to H2
  Go to R1
  Go to next R (railway company)
  Go to next R
  Go to next U (utility company)
  Go back 3 squares.
  The heart of this problem concerns the likelihood of visiting a particular 
  square. That is, the probability of finishing at that square after a roll. 
  For this reason it should be clear that, with the exception of G2J for which 
  the probability of finishing on it is zero, the CH squares will have the 
  lowest probabilities, as 5/8 request a movement to another square, and it is 
  the final square that the player finishes at on each roll that we are 
  interested in. We shall make no distinction between "Just Visiting" and being 
  sent to JAIL, and we shall also ignore the rule about requiring a double to 
  "get out of jail", assuming that they pay to get out on their next turn.

  By starting at GO and numbering the squares sequentially from 00 to 39 we can 
  concatenate these two-digit numbers to produce strings that correspond with 
  sets of squares.

  Statistically it can be shown that the three most popular squares, in order, 
  are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 
  00. So these three most popular squares can be listed with the six-digit modal 
  string: 102400.

  If, instead of using two 6-sided dice, two 4-sided dice are used, find the 
  six-digit modal string.

  Answer:101524 Completed on Mon, 2 Feb 2015, 18:41
  https://projecteuler.net/problem=84
  
  @author Botu Sun
'''
import math, random

dice_faces = 4
total_steps = 1000000

game_board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 
    'JAIL', 'C!', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1',
    'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 
    'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
visit_times = []
# This is not used but the answer is still correct.
# The problem is: three consecutive doubles, do we count 3 + 5 as a double?
# Also do the extra rolls of Community Chest and Chance count for this???
previous_rolls = [1, 1] 
for i in xrange(0, 40):
  visit_times.append([0, str(i) if i >= 10 else '0' + str(i)])
current = 0

def next_with_letter(initial):
  global current
  tmp = (current + 1) % 40
  while not game_board[tmp].startswith(initial):
    tmp = (tmp + 1) % 40
  return tmp

def next_rail():
  return next_with_letter('R')

def next_utility():
  return next_with_letter('U')  


def go():
  global current 
  global previous_rolls
  roll = random.randint(1, dice_faces) + random.randint(1, dice_faces)
  # if (roll % 2 == 0 and previous_rolls[0] % 2 == 0 and 
  #     previous_rolls[1] % 2 == 0):
  #   current = 10
  #   # previous_rolls = [1, 1]
  # else:
  #   current = (current + roll) % 40
  current = (current + roll) % 40
  previous_rolls.pop()
  previous_rolls.insert(0, roll)
  moved = True
  while moved:
    moved = False
    if current == 30: # G2J
      current = 10
      moved = True
    elif current in (2, 17, 33): # CC
      roll = random.randint(1, 16)
      if roll == 1:
        current = 0
        moved = True
      elif roll == 2:
        current = 10
        moved = True
    elif current in (7, 22, 36): # CH
      roll = random.randint(1, 16)
      if roll == 1:
        current = 0
        moved = True
      elif roll == 2:
        current = 10
        moved = True
      elif roll == 3:
        current = 11
        moved = True
      elif roll == 4:
        current = 24
        moved = True
      elif roll == 5:
        current = 39
        moved = True
      elif roll == 6:
        current = 5
        moved = True
      elif roll == 7 or roll == 8:
        current = next_rail()
        moved = True
      elif roll == 9:
        current = next_utility()
        moved = True
      elif roll == 10:
        current = (current - 3) % 40
        moved = True

for i in xrange(0, total_steps):
  visit_times[current][0] += 1
  go()

print ''.join([str(pair[1]) for pair in sorted(visit_times, reverse=True)[:3]])
print sorted(visit_times, reverse=True)