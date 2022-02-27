import numpy as np # numpy is used to make manipulation of the board array easier

from utils import outputPuzzle, loadPuzzle # import functions to output the board and load the board

def validList(array): # checks if the array works as a row, column or square
  temp = [1,2,3,4,5,6,7,8,9] # creates a temporary array full of all possible numbers

  for item in array: # iterate through the input array
    try: # try to remove the item from the temporary array
      temp.remove(item)
    except ValueError: # if the item is not in the temporary array, return false
      return False

  return len(temp) == 0 # if the temporary array is empty, and all items are used, then return true

def validBoard(board): # checks if the board is valid
  for row in board: # for each row
    if not validList(row): # if the row is not valid
      return False
 
  verticalBoard = board.transpose() # allow me to iterate through the board by column

  for column in verticalBoard: # same as for each row, but now by column
    if not validList(column):
      return False

  squareBoard = [ # create a list of all the squares
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

  for square in squareBoard: # same as for each row, but now by square
    if not validList(square):
      return False
  
  return True # if all of the above conditions are met, then the board is valid


def genPossibleValues(sudoku): # generates possible values for each square based on row
  temp_board = [] # create a temporary board

  for x, row in enumerate(sudoku): # for each row
    temp_row = [] # create a temporary row
    for y, item in enumerate(row): # for each item in the row
      if item == 0: # if the item is zero/empty
        temp = [1, 2, 3, 4, 5, 6, 7, 8, 9] # create a temporary array full of all possible numbers
        for i in temp: # iterate through the temporary array
          if i in row or i in sudoku[0:, y] or i in sudoku[x//3*3:x//3*3+3, y//3*3:y//3*3+3].reshape(9): # if the item is in the row/already used
            temp[temp.index(i)] = 0 # remove the item from the temporary array

        while 0 in temp: # while there are still zeros in the temporary array
          temp.remove(0) # remove the zero from the temporary array
      else: # otherwise/if the item is already set
        temp = [item] # set the temporary array to the item
      temp_row.append(temp) # add the temporary array to the temporary row
    temp_board.append(temp_row) # add the temporary row to the temporary board
      
  return np.array(temp_board, dtype=object) # return the temporary board


def genPossibleRows(possibleItems): # generates all possible combinations for each row
  temp_board = [] # create a temporary board

  for row in possibleItems: # for each row
    temp_row = [] # create a temporary row
    for i1 in row[0]: # for each item in the first column
      for i2 in row[1]: # for each item in the second column, and so on
        for i3 in row[2]:
          for i4 in row[3]:
            for i5 in row[4]:
              for i6 in row[5]:
                for i7 in row[6]:
                  for i8 in row[7]:
                    for i9 in row[8]:
                      if validList([i1, i2, i3, i4, i5, i6, i7, i8, i9]): # if the combination is valid
                        temp_row.append([i1, i2, i3, i4, i5, i6, i7, i8, i9]) # add the combination to the temporary row

    temp_board.append(temp_row) # add the temporary row to the temporary board

  return temp_board # return the temporary board

def genPossibleBoard(row): # generates all possible combinations for the board
  temp_board = [] # create a temporary board

  for i1 in row[0]: # for each item in the first column
    for i2 in row[1]: # for each item in the second column, and so on
      for i3 in row[2]:
        for i4 in row[3]:
          for i5 in row[4]:
            for i6 in row[5]:
              for i7 in row[6]:
                for i8 in row[7]:
                  for i9 in row[8]:
                    if validBoard(np.array([i1, i2, i3, i4, i5, i6, i7, i8, i9])): # if the combination is valid
                      temp_board.append([i1, i2, i3, i4, i5, i6, i7, i8, i9]) # add the combination to the temporary board

  return temp_board # return the temporary board

list = loadPuzzle() # load the puzzle

possibleValues = genPossibleValues(list) # create a temporary array to store all possible values for each square

print(outputPuzzle(genPossibleBoard(genPossibleRows(possibleValues))[0])) # generate all possible row combinations, then using those generate all possible board combonations, then print the first valid one