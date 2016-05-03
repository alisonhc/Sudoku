import Remove
import RecursiveRemove
import Solving
import SolveConstraintPropagation
import Generation
import random
import copy
import time


def remove_timing(glist):
    timel = 0.0
    for x in glist:
        start = time.time()
        Remove.remove_numbers(x, 1)
        end = time.time()
        timel = timel + (end - start)
    ftime = timel / 100.0
    return ftime


def rec_remove_timing(glist):
    timel = 0.0
    for x in glist:
        start = time.time()
        RecursiveRemove.rec_remove_numbers(x, random.randint(RecursiveRemove.min_remove(1), RecursiveRemove.max_remove(1)), 0, RecursiveRemove.lowerbound(1), [x for x in range(0, 9)], [x for x in range(0, 9)], [])
        end = time.time()
        timel = timel + (end - start)
    ftime = timel / 100.0
    return ftime


def solve_timing(glist):
    timel = 0.0
    for x in glist:
        start = time.time()
        Solving.solve_grid(x)
        end = time.time()
        timel = timel + (end - start)
    ftime = timel / 100.0
    return ftime


def constraint_solve_timing(glist):
    timel = 0.0
    for x in glist:
        start = time.time()
        SolveConstraintPropagation.constraint_solve(x)
        end = time.time()
        timel = timel + (end - start)
    ftime = timel / 100.0
    return ftime

grids = [Generation.make_full_grid(3) for x in range(0, 500)]

print("Remove time: " + str(remove_timing(copy.deepcopy(grids))))
print("RecursiveRemove time: " + str(rec_remove_timing(copy.deepcopy(grids))))
print("Solving time: " + str(solve_timing(copy.deepcopy(grids))))
print("SolveConstraintPropagation: " + str(constraint_solve_timing(copy.deepcopy(grids))))