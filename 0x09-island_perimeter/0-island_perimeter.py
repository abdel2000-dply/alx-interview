#!/usr/bin/python3
""" Island Perimeter
"""


def island_perimeter(grid):
    """Island Perimeter Function
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check up
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # check down
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
