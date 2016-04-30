import Screen
import Remove
import RecursiveRemove
import Solving
import SolveConstraintPropagation

#A good place to test methods

#grid = Remove.generate_sudoku(1)
#rec_grid = RecursiveRemove.rec_generate_sudoku(1)
#Solving.solve_grid(grid)

Screen.main(SolveConstraintPropagation.display2(SolveConstraintPropagation.constraint_solve(SolveConstraintPropagation.test)))
