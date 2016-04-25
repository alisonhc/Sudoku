import copy
import random
import Generation

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


def remove_numbers(num, difficulty):
    grid = Generation.make_full_grid(num)
    count = 0
    additions = random.randint(min_remove(difficulty), max_remove(difficulty))
    tempgrid = copy.copy(grid)
    while count < additions:
        rando = random.randint(0, 8)
        rando2 = random.randint(0, 8)
        if tempgrid[rando][rando2] is not 0:
            tempgrid[rando][rando2] = 0
            if is_solvable(tempgrid):
                colcount = 0
                for x in range(0, 9):
                    if tempgrid[rando][x] == 0:
                        colcount += 1
                rowcount = 0
                for x in range(0, 9):
                    if tempgrid[x][rando2] == 0:
                        rowcount += 1
                if colcount <= lowerbound(difficulty) and rowcount <= lowerbound(difficulty):
                    grid = copy.copy(tempgrid)
                    count += 1
                else:
                    tempgrid = copy.copy(grid)
    return grid


def is_solvable(grid):
    return True

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
