import json   #imports the array from a universal file
import numpy as np

def outputPuzzle(sudoku):
  s = []

  for row in sudoku:
    temp_row = []
    for item in row: # makes the 0's blanks 
      temp_row.append(" " if item == 0 else item)

    s.append(temp_row)

  res = ""

  res += "+-------+-------+-------+\n"

  res += F"| {s[0][0]} {s[0][1]} {s[0][2]} | {s[0][3]} {s[0][4]} {s[0][5]} | {s[0][6]} {s[0][7]} {s[0][8]} |\n" # creates the sudoku puzzle
  res += F"| {s[1][0]} {s[1][1]} {s[1][2]} | {s[1][3]} {s[1][4]} {s[1][5]} | {s[1][6]} {s[1][7]} {s[1][8]} |\n"
  res += F"| {s[2][0]} {s[2][1]} {s[2][2]} | {s[2][3]} {s[2][4]} {s[2][5]} | {s[2][6]} {s[2][7]} {s[2][8]} |\n"

  res += "|-------+-------|-------|\n"

  res += F"| {s[3][0]} {s[3][1]} {s[3][2]} | {s[3][3]} {s[3][4]} {s[3][5]} | {s[3][6]} {s[3][7]} {s[3][8]} |\n" # creates the sudoku puzzle
  res += F"| {s[4][0]} {s[4][1]} {s[4][2]} | {s[4][3]} {s[4][4]} {s[4][5]} | {s[4][6]} {s[4][7]} {s[4][8]} |\n"
  res += F"| {s[5][0]} {s[5][1]} {s[5][2]} | {s[5][3]} {s[5][4]} {s[5][5]} | {s[5][6]} {s[5][7]} {s[5][8]} |\n"
  
  res += "+-------+-------+-------+\n"

  res += F"| {s[6][0]} {s[6][1]} {s[6][2]} | {s[6][3]} {s[6][4]} {s[6][5]} | {s[6][6]} {s[6][7]} {s[6][8]} |\n" # creates the sudoku puzzle
  res += F"| {s[7][0]} {s[7][1]} {s[7][2]} | {s[7][3]} {s[7][4]} {s[7][5]} | {s[7][6]} {s[7][7]} {s[7][8]} |\n"
  res += F"| {s[8][0]} {s[8][1]} {s[8][2]} | {s[8][3]} {s[8][4]} {s[8][5]} | {s[8][6]} {s[8][7]} {s[8][8]} |\n"
  
  res += "+-------+-------+-------+"

  return res


def validList(array):
  temp = [1,2,3,4,5,6,7,8,9]

  for item in array:
    try:
      temp.remove(item)
    except ValueError:
      return False

  return len(temp) == 0

def validBoard(board):
  for row in board:
    if not validList(row):
      return False

  verticalBoard = board.transpose()

  for column in verticalBoard:
    if not validList(column):
      return False

  squareBoard = [
    board[0:3, 0:3].reshape(9),
    board[0:3, 3:6].reshape(9),
    board[0:3, 6:9].reshape(9),
    board[3:6, 0:3].reshape(9),
    board[3:6, 3:6].reshape(9),
    board[3:6, 6:9].reshape(9),
    board[6:9, 0:3].reshape(9),
    board[6:9, 3:6].reshape(9),
    board[6:9, 6:9].reshape(9)
  ]

  for square in squareBoard:
    if not validList(square):
      return False
  
  return True


def genPossibleRowValues(sudoku):
  temp_board = []

  for row in sudoku:
    temp_row = []
    for item in row:
      if item == 0:
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in temp:
          if i in row:
            temp[temp.index(i)] = 0

        while 0 in temp:
          temp.remove(0)
      else:
        temp = [item]
      temp_row.append(temp)
    temp_board.append(temp_row)
      
  return np.array(temp_board, dtype=object)

def genPossibleColumnValues(s):
  return genPossibleRowValues(s.transpose()).transpose()

def genPossibleSquareValues(board):
  temp_board = []

  for x, row in enumerate(board):
    temp_row = []
    for y, item in enumerate(row):
      if item == 0:
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        square = list[x//3*3:x//3*3+3, y//3*3:y//3*3+3].reshape(9)
        for i in temp:
          if i in square:
            temp[temp.index(i)] = 0

        while 0 in temp:
          temp.remove(0)
      else:
        temp = [item]
      temp_row.append(temp)
    temp_board.append(temp_row)
      
  return np.array(temp_board, dtype=object)


def genPossibleRows(possibleItems):
  temp_board = []

  for row in possibleItems:
    temp_row = []
    for i1 in row[0]:
      for i2 in row[1]:
        for i3 in row[2]:
          for i4 in row[3]:
            for i5 in row[4]:
              for i6 in row[5]:
                for i7 in row[6]:
                  for i8 in row[7]:
                    for i9 in row[8]:
                      if validList([i1, i2, i3, i4, i5, i6, i7, i8, i9]):
                        temp_row.append([i1, i2, i3, i4, i5, i6, i7, i8, i9])

    temp_board.append(temp_row)

  return temp_board

def genPossibleBoard(row):
  temp_board = []

  for i1 in row[0]:
    for i2 in row[1]:
      for i3 in row[2]:
        for i4 in row[3]:
          for i5 in row[4]:
            for i6 in row[5]:
              for i7 in row[6]:
                for i8 in row[7]:
                  for i9 in row[8]:
                    if validBoard(np.array([i1, i2, i3, i4, i5, i6, i7, i8, i9])):
                      temp_board.append([i1, i2, i3, i4, i5, i6, i7, i8, i9])

  return temp_board

list = []

with open('puzzle.json', 'r') as f:
    list = np.array(json.loads(f.read()))

possibleColumnValues = genPossibleColumnValues(list)
possibleRowValues = genPossibleRowValues(list)
possibleSquareValues = genPossibleSquareValues(list)

possibleValues = np.zeros((9, 9), dtype=object)

for x, column in enumerate(possibleColumnValues):
  for y, row in enumerate(column):
    temp = []
    for item in row:
      if item in possibleRowValues[x, y] and item in possibleSquareValues[x, y]:
        temp.append(item)

    possibleValues[x, y] = temp

print(outputPuzzle(genPossibleBoard(genPossibleRows(possibleValues))[0]))