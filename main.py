import json   #imports the array from a universal file
import numpy as np

list = []

with open('puzzle.json', 'r') as f:
    list = np.array(json.loads(f.read()))

def outputPuzzle(sudoku):
  s = []

  for row in sudoku:
    temp_row = []
    for item in row: # makes the 0's blanks 
      temp_row.append(" " if item == 0 else item)

    s.append(temp_row)

  print("+-------+-------+-------+")

  print("|", s[0][0], s[0][1], s[0][2], "|", s[0][3], s[0][4], s[0][5], "|", s[0][6], s[0][7], s[0][8], "|") # creates the sudoku puzzle
  print("|", s[1][0], s[1][1], s[1][2], "|", s[1][3], s[1][4], s[1][5], "|", s[1][6], s[1][7], s[1][8], "|")
  print("|", s[2][0], s[2][1], s[2][2], "|", s[2][3], s[2][4], s[2][5], "|", s[2][6], s[2][7], s[2][8], "|")

  print("|-------+-------|-------|")

  print("|", s[3][0], s[3][1], s[3][2], "|", s[3][3], s[3][4], s[3][5], "|", s[3][6], s[3][7], s[3][8], "|")
  print("|", s[4][0], s[4][1], s[4][2], "|", s[4][3], s[4][4], s[4][5], "|", s[4][6], s[4][7], s[4][8], "|")
  print("|", s[5][0], s[5][1], s[5][2], "|", s[5][3], s[5][4], s[5][5], "|", s[5][6], s[5][7], s[5][8], "|")
  
  print("+-------+-------+-------+")

  print("|", s[6][0], s[6][1], s[6][2], "|", s[6][3], s[6][4], s[6][5], "|", s[6][6], s[6][7], s[6][8], "|")
  print("|", s[7][0], s[7][1], s[7][2], "|", s[7][3], s[7][4], s[7][5], "|", s[7][6], s[7][7], s[7][8], "|")
  print("|", s[8][0], s[8][1], s[8][2], "|", s[8][3], s[8][4], s[0][5], "|", s[8][6], s[8][7], s[8][8], "|")
  
  print("+-------+-------+-------+")

def genPossibleRowValues(sudoku):
  temp_board = []

  for row in sudoku:
    temp_row = []
    for item in row:
      if item == 0:
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in temp:
          if i in row:
            temp.remove(i)
      else:
        temp = [item]
      temp_row.append(temp)
    temp_board.append(temp_row)
      
  return np.array(temp_board, dtype=object)

def genPossibleColumnValues(s):
  board = s.transpose()
  temp_board = []

  for row in board:
    temp_row = []
    for item in row:
      if item == 0:
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in temp:
          if i in row:
            temp.remove(i)
      else:
        temp = [item]
      temp_row.append(temp)
    temp_board.append(temp_row)
      
  return np.array(temp_board, dtype=object).transpose()

print(genPossibleColumnValues(list)[0, 7])
print(genPossibleRowValues(list)[0, 7])