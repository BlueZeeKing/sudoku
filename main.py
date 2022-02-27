import numpy as np

from utils import outputPuzzle, loadPuzzle

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

list = loadPuzzle()

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