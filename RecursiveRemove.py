import copy
import random
import Generation

# This file generates the holes in the Sudoku with recursion
# wrapper function


def rec_generate_sudoku(difficulty):
    grid = Generation.make_full_grid(3)
    additions = random.randint(min_remove(difficulty), max_remove(difficulty))
    return rec_remove_numbers(grid, additions, 0, lowerbound(difficulty), [x for x in range(0, 9)], [x for x in range(0, 9)], [])


def rec_remove_numbers(grid, additions, count, lowerbound, spotsr, spotsc, pairs):
    if count == additions:
        return grid
    else:
        while only_zero_spots(grid, spotsr, spotsc, pairs):
            randor = random.choice(spotsr)
            randoc = random.choice(spotsc)
            if grid[randor][randoc] is not 0 and pair_check(pairs, randor, randoc):
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

                    tempgrid = rec_remove_numbers(copy.deepcopy(grid), additions, count, lowerbound, copy.deepcopy(spotsr), copy.deepcopy(spotsc), copy.deepcopy(pairs))
                    if tempgrid is None:
                        grid[randor][randoc] = removed_num
                        pairs.append([randor, randoc])
                        randor = None
                        randoc = None
                        count -= 1
                    else:
                        return tempgrid
        return None


def pair_check(pairs, randor, randoc):
    pair = True
    for r, c in pairs:
        if r == randor and c == randoc:
            pair = False
    return pair


def only_zero_spots(grid, spotsr, spotsc, pairs):
    zero_count = False
    for r in spotsr:
        for c in spotsc:
            if grid[r][c] is not 0:
                if pair_check(pairs, r, c):
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

test = [[7, 5, 1, 8, 9, 4, 2, 6, 3], [3, 4, 6, 7, 1, 2, 8, 5, 9], [2, 8, 9, 6, 3, 5, 4, 1, 7], [5, 7, 4, 9, 6, 8, 3, 2, 1], [6, 9, 8, 1, 2, 3, 5, 7, 4], [1, 3, 2, 5, 4, 7, 9, 8, 6], [4, 2, 5, 3, 7, 6, 1, 9, 8], [9, 6, 3, 2, 8, 1, 7, 4, 5], [8, 1, 7, 4, 5, 9, 6, 3, 2]]

