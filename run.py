import v0
import v1
import v2

# Test board. See tests.py for more
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

# Flatten the board
board = [item for sublist in board for item in sublist]

# v0
print("===V0===")
v0_board = board.copy()
v0.print_board(v0_board)
if v0.solve(v0_board):
    print("\033[92mSUCCESS\033[0m")
    v0.print_board(v0_board)
else:
    print("\033[91mINVALID\033[0m")

# v1
print("===V1===")
puzzle = v1.SudokuPuzzle(board.copy())
print(puzzle)
if puzzle.solve():
    print("\033[92mSUCCESS\033[0m")
    print(puzzle)
else:
    print("\033[91mINVALID\033[0m")

# v2
print("===V2===")
puzzle = v2.SudokuPuzzle(board.copy())
print(puzzle)
if puzzle.solve():
    print("\033[92mSUCCESS\033[0m")
    print(puzzle)
else:
    print("\033[91mINVALID\033[0m")
