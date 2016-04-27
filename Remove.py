import copy
import random
import Generation


def remove_numbers(num, difficulty):
    grid = Generation.make_full_grid(num)
    count = 0
    additions = random.randint(min_remove(difficulty), max_remove(difficulty))
    tempgrid = copy.copy(grid)
    spotsr = [x for x in range(0, 9)]
    spotsc = [x for x in range(0, 9)]
    while count < additions:
        randor = random.choice(spotsr)
        randoc = random.choice(spotsc)
        if tempgrid[randor][randoc] is not 0:
            removed_number = tempgrid[randor][randoc]
            tempgrid[randor][randoc] = 0
            count += 1
            if is_solvable(tempgrid):
                row_count, col_count = col_and_row_counts(tempgrid, randor, randoc)
                if col_count > lowerbound(difficulty) or row_count > lowerbound(difficulty):
                    if col_count > lowerbound(difficulty):
                        spotsc.remove(randoc)
                    if row_count > lowerbound(difficulty):
                        spotsr.remove(randor)
                    tempgrid[randor][randoc] = removed_number
        #This is the code for checking if the grid can't delete any more spots.
        zero_count = True
        if count > min_remove(difficulty):
            for r in spotsr:
                for c in spotsc:
                    if tempgrid[r][c] is not 0:
                        zero_count = False
            if zero_count:
                count = additions


    return tempgrid

def col_and_row_counts(grid, row, col):
    col_count = 0
    row_count = 0
    for x in range(0, 9):
        if grid[row][x] == 0:
            row_count += 1
    for x in range(0, 9):
        if grid[x][col] == 0:
            col_count += 1
    return row_count, col_count

def is_solvable(grid):
    return True

def min_remove(difficulty):
    if difficulty == 1:
        return 32
    if difficulty == 2:
        return 46
    if difficulty == 3:
        return 50
    if difficulty == 4:
        return 54


def max_remove(difficulty):
    if difficulty == 1:
        return 45
    if difficulty == 2:
        return 49
    if difficulty == 3:
        return 53
    if difficulty == 4:
        return 59

def lowerbound(difficulty):
    if difficulty == 1:
        return 5
    if difficulty == 2:
        return 6
    if difficulty == 3:
        return 7
    if difficulty == 4:
        return 9


print(remove_numbers(3, 1))
