import numpy as np # used for arrays
import json # used for loading the puzzle

from utils import outputPuzzle, loadPuzzle # imports the utils.py file

puzzle = loadPuzzle() # loads the old puzzle

print("The old puzzle was\n", outputPuzzle(puzzle), "", sep="\n") # prints the old puzzle

if input("Do you want to replace it?(y,N) ") == "y": # asks the user if they want to replace the puzzle
  puzzle = np.zeros((9,9), dtype=int) # creates a new puzzle blank puzzle

print("It starts with left to right than up and down. Enter zero for blank spaces.")  # tells the user how to enter the puzzle

for y, row in enumerate(puzzle): # loops through the board
  for x, i in enumerate(row):
    puzzle[y, x] = 10 # sets the current square to 10/solid cursor
    item = input(outputPuzzle(puzzle)) # TODO: make sure the number is valid

    if item == "": # if the user didn't enter anything
      item = 0 # set the item to zero
    else: # otherwise
      item = int(item) # set the item to the number the user entered

    puzzle[y, x] = item # set the current square to the item

print(outputPuzzle(puzzle)) # prints the puzzle

with open('puzzle.json', 'w') as f: # writes the puzzle to a json file
  f.write(json.dumps(puzzle.tolist()))