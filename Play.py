import Screen
import Generation
import Remove
import Solving
import RecursiveRemove
import SolveConstraintPropagation
import copy

#Makes all the code easier to play with

#grid = Generation.make_full_grid(3)
sudoku1 = Remove.generate_sudoku(1)
#sudoku2 = RecursiveRemove.rec_generate_sudoku(1)
solved_sudoku1 = Solving.solve_grid(copy.deepcopy(sudoku1))
#solved_sudoku2 = SolveConstraintPropagation.constraint_solve(copy.deepcopy(sudoku2))
Screen.main(solved_sudoku1)