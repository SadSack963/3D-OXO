import unittest
import oxo_2d
import numpy as np


class TestWin(unittest.TestCase):

    def test_win_column(self):
        print('test_win_column')
        oxo_2d.board = np.array([
            [0, 1, 2],
            [2, 1, 0],
            [0, 1, 0]
        ])
        self.assertEqual(1, oxo_2d.check_win(), "Should be 1")

    def test_win_row(self):
        print('test_win_row')
        oxo_2d.board = np.array([
            [1, 0, 0],
            [2, 2, 2],
            [0, 1, 1]
        ])
        self.assertEqual(2, oxo_2d.check_win(), "Should be 2")

    def test_win_diagonal(self):
        print('test_win_diagonal')
        oxo_2d.board = np.array([
            [1, 2, 2],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.assertEqual(1, oxo_2d.check_win(), "Should be 1")

    def test_win_none(self):
        print('test_win_none')
        oxo_2d.board = np.array([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ])
        self.assertIsNone(oxo_2d.check_win(), "Should be None")

    def test_win_tie(self):
        print('test_win_tie')
        oxo_2d.board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
        ])
        self.assertEqual(0, oxo_2d.check_win(), "Should be 0")

    def test_win_tie_2(self):
        print('test_win_tie')
        oxo_2d.board = np.array([
            [2, 2, 1],
            [1, 1, 2],
            [2, 1, 1]
        ])
        self.assertEqual(0, oxo_2d.check_win(), "Should be 0")


class TestMinimax(unittest.TestCase):

    def test_last_move(self):
        print('test_last_move')
        oxo_2d.board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 0, 2]
        ])
        self.assertEqual((2, 1), oxo_2d.ai_best_move(), "Should be (2, 1)")

    def test_block_win_move(self):
        print('test_block_win_move')
        oxo_2d.board = np.array([
            [1, 1, 2],
            [0, 0, 1],
            [2, 2, 1]
        ])
        self.assertEqual((1, 1), oxo_2d.ai_best_move(), "Should be (1, 1)")

    def test_block_move(self):
        print('test_block_move')
        oxo_2d.board = np.array([
            [1, 2, 0],
            [1, 0, 0],
            [0, 0, 0]
        ])
        self.assertEqual((2, 0), oxo_2d.ai_best_move(), "Should be (2, 0)")

    def test_block_move_2(self):
        print('test_block_move_2')
        oxo_2d.board = np.array([
            [2, 0, 1],
            [1, 1, 0],
            [2, 0, 0]
        ])
        self.assertEqual((1, 2), oxo_2d.ai_best_move(), "Should be (1, 2)")

    def test_win_move(self):
        print('test_win_move')
        oxo_2d.board = np.array([
            [1, 2, 1],
            [1, 2, 0],
            [0, 0, 0]
        ])
        self.assertEqual((2, 1), oxo_2d.ai_best_move(), "Should be (2, 1)")


if __name__ == "__main__":
    unittest.main()
