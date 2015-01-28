# -*- coding: utf-8 -*-
'''
  Path sum: four ways
  Problem 83
  NOTE: This problem is a significantly more challenging version of Problem 81.

  In the 5 by 5 matrix below, the minimal path sum from the top left to the 
  bottom right, by moving left, right, up, and down, is indicated in bold red
  and is equal to 2297.

  [a sample matrix can be found on the original page]

  Find the minimal path sum, in matrix.txt (right click and "Save Link/Target 
  As..."), a 31K text file containing a 80 by 80 matrix, from the top left to 
  the bottom right by moving left, right, up, and down.

  Answer: 425185 Completed on Thu, 29 Jan 2015, 00:26
  https://projecteuler.net/problem=83
  
  @author Botu Sun
'''
import sys

matrix = []
matrix_sum = []
visited = []
visiting = []
visiting.append((0, 0))

# Initialization
for line in open('../res/p083_matrix.txt', 'r'):
  matrix.append([int(n) for n in line[:-1].split(',')])
size = len(matrix)

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
  if y - 1 >= 0: # left
    yield (x, y - 1)
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

print matrix_sum[-1][-1]
