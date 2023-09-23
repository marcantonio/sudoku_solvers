import unittest

import v0
import v1
import v2

tests = [
    [
        True,
        [
            [0,0,0,4,0,0,0,0,0],
            [4,0,9,0,0,6,8,7,0],
            [0,0,0,9,0,0,1,0,0],
            [5,0,4,0,2,0,0,0,9],
            [0,7,0,8,0,4,0,6,0],
            [6,0,0,0,3,0,5,0,2],
            [0,0,1,0,0,7,0,0,0],
            [0,4,3,2,0,0,6,0,5],
            [0,0,0,0,0,5,0,0,0],
        ],
    ],
    [
        False,
        [
            [0,4,0,4,0,0,0,0,0],
            [4,0,9,0,0,6,8,7,0],
            [0,0,0,9,0,0,1,0,0],
            [5,0,4,0,2,0,0,0,9],
            [0,7,0,8,0,4,0,6,0],
            [6,0,0,0,3,0,5,0,2],
            [0,0,1,0,0,7,0,0,0],
            [0,4,3,2,0,0,6,0,5],
            [0,0,0,0,0,5,0,0,0],
        ],
    ],
    [
        False,
        [
            [8,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9],
        ],
    ],
    [
        False,
        [
            [1,0,0,4,0,0,0,0,0],
            [2,0,9,0,0,6,8,7,0],
            [3,0,0,9,0,0,1,0,0],
            [0,0,4,0,2,0,0,0,9],
            [5,7,0,8,0,4,0,6,0],
            [6,0,0,0,3,0,5,0,2],
            [7,0,1,0,0,0,0,0,0],
            [8,4,3,2,0,0,6,0,5],
            [9,0,0,0,0,5,0,0,0],
        ],
    ],
]

class TestSudokuV0(unittest.TestCase):
    def test_solver(self):
        for test in tests:
            board = [item for sublist in test[1] for item in sublist]
            self.assertEqual(test[0], v0.solve(board))

class TestSudokuV1(unittest.TestCase):
    def test_solver(self):
        for test in tests:
            board = [item for sublist in test[1] for item in sublist]
            puzzle = v1.SudokuPuzzle(board)
            self.assertEqual(test[0], puzzle.solve())

class TestSudokuV2(unittest.TestCase):
    def test_solver(self):
        for test in tests:
            board = [item for sublist in test[1] for item in sublist]
            puzzle = v2.SudokuPuzzle(board)
            self.assertEqual(test[0], puzzle.solve())

if __name__ == '__main__':
    unittest.main()
