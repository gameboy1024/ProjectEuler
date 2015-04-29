# -*- coding: utf-8 -*-
'''
  Su Doku
  Problem 96
  
  Su Doku (Japanese meaning number place) is the name given to a popular puzzle 
  concept. Its origin is unclear, but credit must be attributed to Leonhard Euler
  who invented a similar, and much more difficult, puzzle idea called Latin 
  Squares. The objective of Su Doku puzzles, however, is to replace the blanks 
  (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box 
  contains each of the digits 1 to 9. Below is an example of a typical starting 
  puzzle grid and its solution grid.

  [For the two sudoku game matrix, plz go to the original web page]
  
  A well constructed Su Doku puzzle has a unique solution and can be solved by 
  logic, although it may be necessary to employ "guess and test" methods in 
  order to eliminate options (there is much contested opinion over this). The 
  complexity of the search determines the difficulty of the puzzle; the example 
  above is considered easy because it can be solved by straight forward direct 
  deduction.
  
  The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), 
  contains fifty different Su Doku puzzles ranging in difficulty, but all with 
  unique solutions (the first puzzle in the file is the example above).
  
  By solving all fifty puzzles find the sum of the 3-digit numbers found in the 
  top left corner of each solution grid; for example, 483 is the 3-digit number 
  found in the top left corner of the solution grid above.

  Answer: 24702 Completed on Wed, 29 Apr 2015, 22:56
  https://projecteuler.net/problem=96
  
  @author Botu Sun
'''
# Read sudokus into memory
f = open('../res/p096_sudoku.txt', 'r')
sudokus = []
while f.readline():
  sudoku = []
  for i in xrange(0, 9):
    row = []
    l = f.readline()
    for i in xrange(0, 9):
      row.append(int(l[i]))
    sudoku.append(row)
  sudokus.append(sudoku)

def _get_valid_numbers(sudoku, i, j):
  numbers = {}
  for k in xrange(0, 10):
    numbers[k] = True
  for k in xrange(0, 9):
    numbers[sudoku[i][k]] = False
    numbers[sudoku[k][j]] = False
  anchor_x, anchor_y = i / 3 * 3, j / 3 * 3
  for k in xrange(0, 9):
    m = anchor_x + k / 3
    n = anchor_y + k % 3
    numbers[sudoku[m][n]] = False
  result = []
  for k, v in numbers.items():
    if v == True:
      result.append(k)
  return result

def recursion(sudoku, i):
  if i == 81:
    return True
  while sudoku[i / 9][i % 9] != 0:
    i += 1
    if i == 81:
      return True
  for j in _get_valid_numbers(sudoku, i / 9, i % 9):
    sudoku[i / 9][i % 9] = j
    if recursion(sudoku, i + 1):
      return True
  sudoku[i / 9][i % 9] = 0
  return False

total = 0
for sudoku in sudokus:
  recursion(sudoku, 0)
  total += sudoku[0][0] * 100 + sudoku[0][1] * 10 + sudoku[0][2]
print total
  