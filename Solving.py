# from Generation import *
# from Remove import *
import math
import random


"""def solve_grid(grid):
    dimen = len(grid)
    num = int(math.sqrt(dimen))
    # new_grid = [[None for _ in range(dimen)] for _ in range(dimen)]

    def fill(index):
        curr_row, curr_column = divmod(index, dimen)
        r1, c1 = curr_row - (curr_row % 3), curr_column - (curr_column % 3)
        numbers = list(range(1, dimen + 1))
        random.shuffle(numbers)
        for n in numbers: # it definitely enters this for loop
            if index + 1 >= dimen ** 2:  # or fill(index + 1):
                print('base case')
                return grid
            if (grid[curr_row][curr_column] == 0) and (n not in grid[curr_row] and all(row[curr_column] != n for row in grid)
            and all(n not in row[c1:c1 + num] for row in grid[r1:curr_row])):
                grid[curr_row][curr_column] = n
                print('work')
            f = fill(index+1)
            if f == 0:
                print('yo')
                grid[curr_row][curr_column] = 0
            else:
                print('c')
                return f

      #  else:
      #     grid[curr_row][curr_column] = 0
       #    return 0
    return fill(0)"""


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
        for n in numbers:
            if (grid[curr_row][curr_column] == 0) and (n not in grid[curr_row] and all(row[curr_column] != n for row in grid)
            and all(n not in row[c1:c1 + num] for row in grid[r1:curr_row])):
                grid[curr_row][curr_column] = n
                print('work')
            if index + 1 >= dimen ** 2 or fill(index + 1):
                print('f')
                return grid

        print('backtrack')
        grid[curr_row][curr_column] = 0
        return None

    return fill(0)



def has_unique_solution():
    return True


test = [[5, 6, 4, 9, 8, 3, 0, 0, 0], [9, 8, 1, 0, 2, 0, 0, 3, 4], [7, 0, 3, 1, 5, 0, 9, 8, 6], [3, 0, 6, 0, 7, 9, 0, 0, 0], [1, 4, 0, 5, 6, 0, 0, 0, 0], [2, 7, 0, 3, 4, 1, 8, 6, 5], [0, 0, 2, 0, 0, 0, 0, 5, 3], [0, 9, 0, 0, 0,5, 6, 0, 0], [8, 3, 0, 7, 0, 6, 4, 0, 9]]
grid = [[None for _ in range(9)] for _ in range(9)]
# print(test)
print(solve_grid(test))
# print(test)


