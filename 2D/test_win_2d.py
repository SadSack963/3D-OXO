import unittest
import oxo_2d
import numpy as np


class TestWin(unittest.TestCase):

    def test_win_column(self):
        print('test_win_column')
        user = 1
        oxo_2d.board = np.array([
            [0, 1, 2],
            [2, 1, 0],
            [0, 1, 0]
        ])
        self.assertEqual(1, oxo_2d.check_win(), "Should be 1")

    def test_win_row(self):
        print('test_win_row')
        user = 2
        oxo_2d.board = np.array([
            [1, 0, 0],
            [2, 2, 2],
            [0, 1, 1]
        ])
        self.assertEqual(2, oxo_2d.check_win(), "Should be 2")

    def test_win_diagonal(self):
        print('test_win_diagonal')
        user = 1
        oxo_2d.board = np.array([
            [1, 2, 2],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.assertEqual(1, oxo_2d.check_win(), "Should be 1")

    def test_win_none(self):
        print('test_win_none')
        user = 2
        oxo_2d.board = np.array([
            [0, 2, 0],
            [1, 2, 1],
            [0, 1, 0]
        ])
        self.assertEqual(None, oxo_2d.check_win(), "Should be None")

    def test_win_tie(self):
        print('test_win_tie')
        user = 2
        oxo_2d.board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
        ])
        self.assertEqual(0, oxo_2d.check_win(), "Should be 0")


if __name__ == "__main__":
    unittest.main()
