# from Generation import *
# from Remove import *
import math
import random

# Solves the sudoku game
def solve_grid(grid):
    dimen = len(grid)
    num = int(math.sqrt(dimen))

    def fill(index):
        curr_row, curr_column = divmod(index, dimen)
        # make num*num block (like in Sudoku grid)
        r1, c1 = curr_row - (curr_row % 3), curr_column - (curr_column % 3)
        # create list of numbers 1 through dimen. so in traditional Sudoku 1-9
        numbers = list(range(1, dimen + 1))
        random.shuffle(numbers)
        if grid[curr_row][curr_column] == 0:
            for n in numbers:
                if (n not in grid[curr_row] and all(row[curr_column] != n for row in grid)
                and all(n not in row[c1:c1 + num] for row in grid[r1:r1 + num])):
                    grid[curr_row][curr_column] = n
                    if index + 1 >= dimen ** 2 or fill(index + 1):
                        return grid
            grid[curr_row][curr_column] = 0
            return None
        else:
            if index + 1 >= dimen ** 2 or fill(index + 1):
                return grid

    return fill(0)

test = [[5, 6, 4, 9, 8, 3, 0, 0, 0], [9, 8, 1, 0, 2, 0, 0, 3, 4], [7, 0, 3, 1, 5, 0, 9, 8, 6], [3, 0, 6, 0, 7, 9, 0, 0, 0], [1, 4, 0, 5, 6, 0, 0, 0, 0], [2, 7, 0, 3, 4, 1, 8, 6, 5], [0, 0, 2, 0, 0, 0, 0, 5, 3], [0, 9, 0, 0, 0,5, 6, 0, 0], [8, 3, 0, 7, 0, 6, 4, 0, 9]]




