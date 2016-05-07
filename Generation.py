import random


# Generates the full grid that we will later poke holes into
def make_full_grid(num):  # cannot just have dimen at input; need to know num later in function
    """Return a random filled num**2 n num**2 Sudoku grid."""
    dimen = num ** 2
    # initialize list of dimen lists, each with dimen elements, all elements being None
    # this list of lists represents an empty Sudoku grid
    # (basically a 2d array)
    # each list within the big list represents a row
    grid = [[None for _ in range(dimen)] for _ in range(dimen)]

    def fill_grid(index):  # input is index in grid, so when you call it you start it at 0
        # divmod: take two numbers as arguments and return a pair of numbers consisting of their
        # quotient and remainder when using integer division. index of row, index
        curr_row, curr_column = divmod(index, dimen)
        # make num*num block (like in Sudoku grid)
        r1, c1 = curr_row - (curr_row % 3), curr_column - (curr_column % 3)
        # create list of numbers 1 through dimen. so in traditional Sudoku 1-9
        numbers = list(range(1, dimen + 1))
        random.shuffle(numbers)
        for n in numbers:
            # all(): return True if all elements in iterable are true (or if iterable is empty)
            # if n is not in row, column, or block
            if (n not in grid[curr_row] and all(row[curr_column] != n for row in grid)
            and all(n not in row[c1:c1 + num] for row in grid[r1:r1 + num])):
                grid[curr_row][curr_column] = n  # put n into spot
                if index + 1 >= dimen ** 2 or fill_grid(index + 1):  # if index has gone thru entire grid
                    return grid
        # backtrack, resetting spot to None
        grid[curr_row][curr_column] = None
        return None

    return fill_grid(0)

