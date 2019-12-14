grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

height = len(grid)
width = len(grid[1])

# Grid as is
for y in range(height):
    for x in range(width):
        print(grid[y][x], end="")
    print()

print()

# Grid tilted 90' right
for x in range(width):
    for y in range(height):
        print(grid[y][x], end="")
    print()




