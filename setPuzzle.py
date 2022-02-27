import numpy as np
import json

from utils import outputPuzzle, loadPuzzle

puzzle = loadPuzzle()

print("The old puzzle was\n", outputPuzzle(puzzle), "", sep="\n")

if input("Do you want to replace it?(y,N) ") == "y":
  puzzle = np.zeros((9,9), dtype=int)

print("It starts with left to right than up and down. Enter zero for blank spaces.")

for y, row in enumerate(puzzle):
  for x, i in enumerate(row):
    puzzle[y, x] = 10
    item = input(outputPuzzle(puzzle)) # TODO: make sure the number is valid

    if item == "":
      item = 0
    else:
      item = int(item)

    puzzle[y, x] = item

outputPuzzle(puzzle)

with open('puzzle.json', 'w') as f:
  f.write(json.dumps(puzzle.tolist()))