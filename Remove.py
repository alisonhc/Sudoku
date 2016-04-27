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
            replacedValue = tempgrid[randor][randoc]
            tempgrid[randor][randoc] = 0
            count += 1
            if is_solvable(tempgrid):
                rowcount,colcount = getRowAndColumnCount(tempgrid,randor,randoc)
                if colcount > lowerbound(difficulty) or rowcount > lowerbound(difficulty):
                    if colcount > lowerbound(difficulty):
                        spotsc.remove(randoc)
                    if rowcount > lowerbound(difficulty):
                        spotsr.remove(randor)
                    tempgrid[randor][randoc] = replacedValue
                    count -= 1

    return tempgrid

def getRowAndColumnCount(grid,row,column):
    rowcount = 0
    colcount = 0
    for x in range(0, 9):
        if grid[row][x] == 0:
            rowcount += 1
    for x in range(0, 9):
        if grid[x][column] == 0:
            colcount += 1
    return (rowcount,colcount)

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
