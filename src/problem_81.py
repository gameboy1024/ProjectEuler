# -*- coding: utf-8 -*-
'''
  Path sum: two ways
  Problem 81
  In the 5 by 5 matrix below, the minimal path sum from the top left to the 
  bottom right, by only moving to the right and down, is indicated in bold red 
  and is equal to 2427.

  [a matrix can be found on initial page]

  Find the minimal path sum, in matrix.txt (right click and "Save Link/Target 
    As..."), a 31K text file containing a 80 by 80 matrix, from the top left to 
  the bottom right by only moving right and down.

  Answer: 427337 Completed on Wed, 28 Jan 2015, 23:42
  https://projecteuler.net/problem=81
  
  @author Botu Sun
'''
import sys
matrix = []
f = open('../res/p081_matrix.txt', 'r')
for line in f:
  matrix.append([int(n) for n in line[:-1].split(',')])
size = len(matrix)

matrix_sum = []
for i in xrange(0, size):
  matrix_sum.append([0] * size)
matrix_sum[0][0] = matrix[0][0]

def next_points(x, y):
  global size
  result = []
  # if x - 1 > 0: # left
  #   result.append((x - 1, y))
  if x + 1 < size: # right
    result.append((x + 1, y))
  # if y - 1 > 0: # up
  #   result.append((x, y - 1))
  if y + 1 < size: # down
    result.append((x, y + 1))
  return result

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

current = (0, 0)
visited = []
visiting = [current]

while len(visiting):
  x, y = find_min(visiting, matrix_sum)
  visited.append((x, y))
  visiting.remove((x, y))

  points = next_points(x, y)
  for p in points:
    value = matrix_sum[x][y] + matrix[p[0]][p[1]]
    if p not in visiting and p not in visited:
      matrix_sum[p[0]][p[1]] = value
      visiting.append(p)
    if value < matrix_sum[p[0]][p[1]]:
      matrix_sum[p[0]][p[1]] = value

print matrix_sum[-1][-1]