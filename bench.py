import timeit
from cProfile import Profile
from pstats import SortKey, Stats

import v0
import v1
import v2

board = [
    [0,0,0,4,0,0,0,0,0],
    [4,0,9,0,0,6,8,7,0],
    [0,0,0,9,0,0,1,0,0],
    [5,0,4,0,2,0,0,0,9],
    [0,7,0,8,0,4,0,6,0],
    [6,0,0,0,3,0,5,0,2],
    [0,0,1,0,0,7,0,0,0],
    [0,4,3,2,0,0,6,0,5],
    [0,0,0,0,0,5,0,0,0],
]
board = [item for sublist in board for item in sublist]
num_runs = 100

# v0
def v0_func():
    v0_board = board.copy()
    v0.solve(v0_board)

dur = timeit.Timer(v0_func).timeit(number = num_runs)
print(f"v0: f{dur/num_runs:.{3}}s")

# v1
def v1_func():
    puzzle = v1.SudokuPuzzle(board)
    puzzle.solve()

dur = timeit.Timer(v1_func).timeit(number = num_runs)
print(f"v1: f{dur/num_runs:.{3}}s")

# v2
def v2_func():
    puzzle = v2.SudokuPuzzle(board.copy())
    puzzle.solve()

dur = timeit.Timer(v2_func).timeit(number = num_runs)
print(f"v2: f{dur/num_runs:.{3}}s")
