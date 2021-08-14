import unittest
import oxo_2d
import numpy as np


class TestWin(unittest.TestCase):

    def test_win_column(self):
        print('test_win_column')
        user = 1
        oxo_2d.board = np.zeros(shape=(3, 3), dtype=int)
        # array([[0, 0, 0],
        #        [0, 0, 0],
        #        [0, 0, 0]])
        for i in range(3):
            oxo_2d.board[i][1] = user
        print(oxo_2d.board)
        self.assertEqual(1, oxo_2d.check_win(user), "Should be 1")

    def test_win_row(self):
        print('test_win_row')
        user = 2
        oxo_2d.board = np.zeros(shape=(3, 3), dtype=int)
        # array([[0, 0, 0],
        #        [0, 0, 0],
        #        [0, 0, 0]])
        for i in range(3):
            oxo_2d.board[2][i] = user
        print(oxo_2d.board)
        self.assertEqual(2, oxo_2d.check_win(user), "Should be 2")

    def test_win_diagonal(self):
        print('test_win_diagonal')
        user = 1
        oxo_2d.board = np.zeros(shape=(3, 3), dtype=int)
        # array([[0, 0, 0],
        #        [0, 0, 0],
        #        [0, 0, 0]])
        for i in range(3):
            oxo_2d.board[i][2-i] = user
        print(oxo_2d.board)
        self.assertEqual(1, oxo_2d.check_win(user), "Should be 1")

    def test_win_none(self):
        print('test_win_none')
        user = 2
        oxo_2d.board = np.zeros(shape=(3, 3), dtype=int)
        # array([[0, 0, 0],
        #        [0, 0, 0],
        #        [0, 0, 0]])
        for i in range(1, 3):
            oxo_2d.board[i][2-i] = user
        print(oxo_2d.board)
        self.assertEqual(None, oxo_2d.check_win(user), "Should be None")

    def test_win_tie(self):
        print('test_win_tie')
        user = 2
        oxo_2d.board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
        ])
        print(oxo_2d.board)
        self.assertEqual(0, oxo_2d.check_win(user), "Should be 0")


if __name__ == "__main__":
    unittest.main()
