# Conways game of life
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
        if random.randint(0, 1) == 0:
            column.append('#')  # Add a living cell
        else:
            column.append(" ")  # Add a dead cell
    next_cells.append(column)

# Main program loop
while True:
    print("\n" * 5)  # Separates each step with newlines
    current_cells = copy.deepcopy(next_cells)
    # Print current_cells on the screen
    for x in range(width):
        for y in range(height):
            print(current_cells[x][y], end="")  # Print the # or space.
        print()

    # Calculate the next step's cells based on current step's  cells
    for x in range(width):
        for y in range(height):
            # Get neighboring coordinates:
            # % width ensures left-coord is always between 0 and width - 1
            left_coord = (x - 1) % width
            right_coord = (x + 1) % width
            above_coord = (y - 1) % height
            below_coord = (y + 1) % height

            # Count number of numbering neighbors:
            num_neighbors = 0
            if current_cells[left_coord][above_coord]:  # Top-left neighbor is alive
                num_neighbors += 1
            if current_cells[x][above_coord]:  # Top neighbor is alive
                num_neighbors += 1
            if current_cells[right_coord][above_coord]:  # Top-right neighbor is alive
                num_neighbors += 1
            if current_cells[left_coord][y]:  # left neighbor is alive
                num_neighbors += 1
            if current_cells[right_coord][y]:  # Right neighbor is alive
                num_neighbors += 1
            if current_cells[left_coord][below_coord]:  # Bottom-left neighbor is alive
                num_neighbors += 1
            if current_cells[x][below_coord]:  # Bottom neighbor is alive
                num_neighbors += 1
            if current_cells[right_coord][below_coord]:  # Bottom-right neighbor is alive
                num_neighbors += 1

            # Set cell based on Conway's Game of Life rules:
            if current_cells[x][y] == "#" and (
                    num_neighbors == 2 or num_neighbors == 3):  # Living cells with 2 or 3 neighbors stay alive
                next_cells[x][y] = "#"
            elif current_cells[x][y] == " " and num_neighbors == 3:  # Dead cells with 3 neighbors becomes alive
                next_cells[x][y] = "#"
            else:  # Everything else dies or stays dead
                next_cells = " "
    time.sleep(1)  # Adds 1 second pause to reduce flickering
