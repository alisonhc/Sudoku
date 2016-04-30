# code to fancilly solve sudoku

# make [A1, A2, A3....]
def cross(A, B):
    return [a+b for a in A for b in B]


# SHOULD MAKE A WRAPPER FUNCTION FOR ALL THIS STUFF
digits = '123456789'
rows = 'ABCDEFGHI'
columns = digits
tiles = cross(rows, columns)  # [A1, A2, A3....]
columns_array = ([cross(rows, c) for c in columns] +  # [[All the ones], [All the twos],....] columns
            [cross(r, columns) for r in rows] +
                 [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in columns_array if s in u])  # all tiles that each tile runs into (row, column, square)
             for s in tiles)
tiles_in_vicinity = dict((s, set(sum(units[s], [])) - set([s]))  # {tile: tiles that share at least one unit with it}
                         for s in tiles)                      # tiles that have whose units intersect


def constraint_solve(grid):
    """Convert grid to a dict of possible values, {spot: digits}, or
    return False"""
    possible_values = dict((spot, digits) for spot in tiles)     # {'A2': '123456789', 'B9': '123456789', 'B6': '123456789', ...]
    for spot,num in grid_values(grid).items():           # iterate over this dictionary's keys and values
        if num in digits and not assign(possible_values, spot, num):
            return False  # fail if we can't assign num to this spot
    return possible_values


# EDIT TO TAKE ARRAY INSTEAD OF STRING
def grid_values(grid):
    vals = ''
    for x in range(0, 9):
        for y in range(0, 9):
            i = grid[x][y]
            vals += str(i)
    """Convert grid into a dict of {tile: number} with '0' for empty spots"""
    # {'I1': '0', 'E5': '0', 'B9': '1', 'H6': '3',...}
    puzzle = [c for c in vals if c in digits or c in '0']
    return dict(zip(tiles, puzzle))


def assign(possible_vals, spot, num):  # spot is the key, num is the value
    """Eliminate all the other values (except num) from values[spot] and do the constraint propagation thingy.
    Return values, except return False when this is impossible"""
    # eliminate all but one value from possible_vals, so that that particular tile is solved
    other_values = possible_vals[spot].replace(num, '')  # replace(old substring, new substring). so all values besides num
    if all(eliminate_possibilities(possible_vals, spot, num2) for num2 in other_values):  # if all other nums can be eliminated as possibilities
        return possible_vals
    else:
        return False


def eliminate_possibilities(possible_vals, spot, num):
    if num not in possible_vals[spot]:
        return possible_vals  # this number has already been eliminated
    possible_vals[spot] = possible_vals[spot].replace(num, '')    # remove num from possibilities
    # if only num2 works with particular tile, then eliminate num from the peers
    if len(possible_vals[spot]) == 0:
        return False  # removed last value! not okay
    elif len(possible_vals[spot]) == 1:
        num2 = possible_vals[spot]
        if not all(eliminate_possibilities(possible_vals, spot2, num2) for spot2 in tiles_in_vicinity[spot]):
            return False
    # if a unit u has only one available spot for num, then put it there
    for u in units[spot]:
        available_places = [s for s in u if num in possible_vals[s]]
        if len(available_places) == 0:
            return False  # No place for this value?! no way
        elif len(available_places) == 1:
            if not assign(possible_vals, available_places[0], num):  # this recurses too, because assign calls eliminate
                return False    # I LOOKED UP THIS IF STATEMENT HERE: did not think of it myself
    return possible_vals


# ALISON DID NOT WRITE THIS. SHE FOUND IT ONLINE FOR TESTING PURPOSES. we can remove it soon
def display(values):
    "Display these values as a 2-D grid."
    width = 1+max(len(values[s]) for s in tiles)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print (''.join(values[r+c].center(width) + ('|' if c in '36' else '')
                       for c in columns))
        if r in 'CF': print(line)
    print
def display2(values):
    solvedgrid = [[None for _ in range(9)] for _ in range(9)]
    count = 0
    for x in 'ABCDEFGHI':
        for y in range(1, 10):
            solvedgrid[count][y-1] = values[x+str(y)]
        count += 1
    return solvedgrid
test = [[5, 6, 4, 9, 8, 3, 0, 0, 0], [9, 8, 1, 0, 2, 0, 0, 3, 4], [7, 0, 3, 1, 5, 0, 9, 8, 6], [3, 0, 6, 0, 7, 9, 0, 0, 0], [1, 4, 0, 5, 6, 0, 0, 0, 0], [2, 7, 0, 3, 4, 1, 8, 6, 5], [0, 0, 2, 0, 0, 0, 0, 5, 3], [0, 9, 0, 0, 0,5, 6, 0, 0], [8, 3, 0, 7, 0, 6, 4, 0, 9]]
# FOUND THIS EXAMPLE ONLINE FOR TESTING PURPOSES. Mark you can hook it up
grid1 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300'
test2 = [[0,0,3,0,2,0,6,0,0],[9,0,0,3,0,5,0,0,1],[0,0,1,8,0,6,4,0,0],[0,0,8,1,0,2,9,0,0],[7,0,0,0,0,0,0,0,8],[0,0,6,7,0,8,2,0,0],[0,0,2,6,0,9,5,0,0],[8,0,0,2,0,3,0,0,9],[0,0,5,0,1,0,3,0,0]]
'0030206090030500001806400081029070000000006708200026095080020300'

display2(constraint_solve(test))
"""def back_to_array(solved):
    array = [[None for _ in range(9)] for _ in range(9)]
    for r in rows:"""


