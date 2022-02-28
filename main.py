import numpy as np # numpy is used to make manipulation of the board array easier
import time # used for timing the program
from utils import outputPuzzle, loadPuzzle # import functions to output the board and load the board

def validPlacement(board, row, column, value): # checks if the placement is valid
  return not (value in board[row, :] or value in board[:, column] or value in board[row//3*3:row//3*3+3, column//3*3:column//3*3+3].reshape(9))

def genPossibleValues(sudoku): # generates possible values for each square based on row
  temp_board = [] # create a temporary board

  for x, row in enumerate(sudoku): # for each row
    temp_row = [] # create a temporary row
    for y, item in enumerate(row): # for each item in the row
      if item == 0: # if the item is zero/empty
        temp = [] # create a temporary array full of all possible numbers
        for i in range(1,10): # iterate through the temporary array
          if validPlacement(sudoku, x, y, i): # if the item is in the row/already used
            temp.append(i) # remove the item from the temporary array

      else: # otherwise/if the item is already set
        temp = [item] # set the temporary array to the item
      temp_row.append(temp) # add the temporary array to the temporary row
    temp_board.append(temp_row) # add the temporary row to the temporary board
      
  return np.array(temp_board, dtype=object) # return the temporary board

def solve(grid, possible, row = 0, col = 0): 
  if row == 8 and col == 9: # if the end has been reached
    return True # return true

  if col == 9: # if the end of the column has been reached
    row += 1 # move to the next row
    col = 0 # reset the column

  if grid[row, col] != 0: # if the square is already set
    return solve(grid, possible, row, col + 1) # move to the next square

  for item in possible[row, col]: # for each item in the square
    if validPlacement(grid, row, col, item): # if the placement is valid
      grid[row, col] = item # set the square to the item

      if solve(grid, possible, row, col + 1): # if the next square is valid
        return True # return true

    grid[row, col] = 0 # otherwise, set the square to zero

  return False # if none of the items are valid, return false

list = loadPuzzle() # load the puzzle

start_time = time.time() # start the timer

possibleValues = genPossibleValues(list) # create a temporary array to store all possible values for each square

print(outputPuzzle(list) if solve(list, possibleValues) else "No solution found") # solve the puzzle

print(time.time() - start_time) # print the time it took to solve the puzzle