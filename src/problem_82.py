# -*- coding: utf-8 -*-
'''
  Path sum: three ways
  Problem 82
  NOTE: This problem is a more challenging version of Problem 81.

  The minimal path sum in the 5 by 5 matrix below, by starting in any cell in 
  the left column and finishing in any cell in the right column, and only moving
  up, down, and right, is indicated in red and bold; the sum is equal to 994.

  [a sample matrix can be found on the original page]

  Find the minimal path sum, in matrix.txt (right click and "Save Link/Target 
  As..."), a 31K text file containing a 80 by 80 matrix, from the left column 
  to the right column.

  Answer: 260324 Completed on Thu, 29 Jan 2015, 00:21
  https://projecteuler.net/problem=82
  
  @author Botu Sun
'''
import sys

matrix = []
matrix_sum = []
visited = []
visiting = []

# Initialization
for line in open('../res/p082_matrix.txt', 'r'):
  matrix.append([int(n) for n in line[:-1].split(',')])
size = len(matrix)

for i in xrange(0, size):
  visiting.append((i, 0))

for i in xrange(0, size):
  matrix_sum.append([0] * size)

for p in visiting:
  matrix_sum[p[0]][p[1]] = matrix[p[0]][p[1]]

def adjacent_points(x, y):
  global size
  if x - 1 >= 0: # up
    yield (x - 1, y)
  if x + 1 < size: # down
    yield (x + 1, y)
  # if y - 1 >= 0: # left
    # yield (x, y - 1)
  if y + 1 < size: # right
    yield (x, y + 1)

def find_min(visiting, matrix_sum):
  min_x = -1
  min_y = -1
  min = sys.maxint
  for point in visiting:
    if matrix_sum[point[0]][point[1]] < min:
      min = matrix_sum[point[0]][point[1]]
      min_x = point[0]
      min_y = point[1]
  return min_x, min_y

while len(visiting):
  x, y = find_min(visiting, matrix_sum)
  visited.append((x, y))
  visiting.remove((x, y))
  for p in adjacent_points(x, y):
    value = matrix_sum[x][y] + matrix[p[0]][p[1]]
    if p not in visiting and p not in visited:
      matrix_sum[p[0]][p[1]] = value
      visiting.append(p)
    if value < matrix_sum[p[0]][p[1]]:
      matrix_sum[p[0]][p[1]] = value

min = sys.maxint
for i in xrange(0, size):
  if matrix_sum[i][-1] < min:
    min = matrix_sum[i][-1]
print min
