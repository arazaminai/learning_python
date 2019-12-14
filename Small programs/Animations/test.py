import copy
import random
import time

width = 60
height = 60

# Create a list of lists for the cell
next_cells = []
for x in range(width):
    column = []  # Create a new column
    for y in range(height):
        column.append(y)
        next_cells.append(column)
        print(next_cells[y])