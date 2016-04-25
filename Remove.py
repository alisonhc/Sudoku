import copy
import random
import Generation


def remove_numbers(num, difficulty):
    grid = Generation.make_full_grid(num)
    count = 0
    additions = random.randint(min_remove(difficulty), max_remove(difficulty))
    print(additions)
    tempgrid = copy.copy(grid)
    spotsr = [x for x in range(0, 9)]
    spotsc = [x for x in range(0, 9)]
    while count < additions:
        randor = random.choice(spotsr)
        randoc = random.choice(spotsc)
        if tempgrid[randor][randoc] is not 0:
            tempgrid[randor][randoc] = 0
            if is_solvable(tempgrid):
                rowcount = 0
                for x in range(0, 9):
                    if tempgrid[randor][x] == 0:
                        rowcount += 1
                colcount = 0
                for x in range(0, 9):
                    if tempgrid[x][randoc] == 0:
                        colcount += 1
                if colcount <= lowerbound(difficulty) and rowcount <= lowerbound(difficulty):
                    grid = copy.copy(tempgrid)
                    count += 1
                    print(count)
                if colcount > lowerbound(difficulty):
                    spotsc.remove(randoc)
                    tempgrid = copy.copy(grid)
                if rowcount > lowerbound(difficulty):
                    spotsr.remove(randor)
                    tempgrid = copy.copy(grid)

    return grid


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


print(remove_numbers(3, 2))
