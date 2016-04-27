import copy
import random
import Generation

def generate_sudoku(difficulty):
    grid = Generation.make_full_grid(3)
    additions = random.randint(min_remove(difficulty), max_remove(difficulty))
    return rec_remove_numbers(grid, additions, 0, lowerbound(difficulty), [x for x in range(0, 9)], [x for x in range(0, 9)], min_remove(difficulty))

def rec_remove_numbers(grid, additions, count, lowerbound, spotsr, spotsc, min):
    if count == additions:
        return grid
    else:
        while only_zero_spots(grid, spotsr, spotsc):
            randor = random.choice(spotsr)
            randoc = random.choice(spotsc)
            if grid[randor][randoc] is not 0:
                removed_num = grid[randor][randoc]
                grid[randor][randoc] = 0
                count += 1
                row_count, col_count = col_and_row_counts(grid, randor, randoc)
                if col_count > lowerbound or row_count > lowerbound:
                    if col_count > lowerbound:
                        spotsc.remove(randoc)
                    if row_count > lowerbound:
                        spotsr.remove(randor)
                    grid[randor][randoc] = removed_num
                    count -= 1
                else:
                    tempgrid = rec_remove_numbers(grid, additions, count, lowerbound, spotsr, spotsc, min)
                    if tempgrid is None:
                        grid[randor][randoc] = removed_num
                        count -= 1
                    else:
                        return tempgrid
        return None

def only_zero_spots(grid, spotsr, spotsc):
    zero_count = False
    for r in spotsr:
        for c in spotsc:
            if grid[r][c] is not 0:
                zero_count = True

    return zero_count


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


print(generate_sudoku(1))
