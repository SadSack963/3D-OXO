import unittest
import oxo_2d
import numpy as np
from evaluate_board_state import evaluate_board
import global_vars

class TestWin(unittest.TestCase):

    def test_win_column(self):
        print('test_win_column')
        board = np.array([
            [0, 1, 2],
            [2, 1, 0],
            [0, 1, 0]
        ])
        self.assertEqual(1, evaluate_board(board), "Should be 1")

    def test_win_row(self):
        print('test_win_row')
        board = np.array([
            [1, 0, 0],
            [2, 2, 2],
            [0, 1, 1]
        ])
        self.assertEqual(2, evaluate_board(board), "Should be 2")

    def test_win_diagonal(self):
        print('test_win_diagonal')
        board = np.array([
            [1, 2, 2],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.assertEqual(1, evaluate_board(board), "Should be 1")

    def test_win_none(self):
        print('test_win_none')
        board = np.array([
            [1, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ])
        self.assertIsNone(evaluate_board(board), "Should be None")

    def test_win_tie(self):
        print('test_win_tie')
        board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 1, 2]
        ])
        self.assertEqual(0, evaluate_board(board), "Should be 0")

    def test_win_tie_2(self):
        print('test_win_tie')
        board = np.array([
            [2, 2, 1],
            [1, 1, 2],
            [2, 1, 1]
        ])
        self.assertEqual(0, evaluate_board(board), "Should be 0")


class TestMinimax(unittest.TestCase):

    def test_last_move(self):
        print('test_last_move')
        global_vars.board = np.array([
            [1, 2, 1],
            [1, 1, 2],
            [2, 0, 2]
        ])
        ai_player = oxo_2d.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((2, 1), (ai_player.row, ai_player.col), "Should be (2, 1)")

    def test_block_win_move(self):
        print('test_block_win_move')
        global_vars.board = np.array([
            [1, 1, 2],
            [0, 0, 1],
            [2, 2, 1]
        ])
        ai_player = oxo_2d.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((1, 1), (ai_player.row, ai_player.col), "Should be (1, 1)")

    def test_block_move(self):
        print('test_block_move')
        global_vars.board = np.array([
            [1, 2, 0],
            [1, 0, 0],
            [0, 0, 0]
        ])
        ai_player = oxo_2d.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((2, 0), (ai_player.row, ai_player.col), "Should be (2, 0)")

    def test_block_move_2(self):
        print('test_block_move_2')
        global_vars.board = np.array([
            [2, 0, 1],
            [1, 1, 0],
            [2, 0, 0]
        ])
        ai_player = oxo_2d.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((1, 2), (ai_player.row, ai_player.col), "Should be (1, 2)")

    def test_win_move(self):
        print('test_win_move')
        global_vars.board = np.array([
            [1, 2, 1],
            [1, 2, 0],
            [0, 0, 0]
        ])
        ai_player = oxo_2d.AIPlayer(2)
        ai_player.get_move()
        self.assertEqual((2, 1), (ai_player.row, ai_player.col), "Should be (2, 1)")


if __name__ == "__main__":
    unittest.main()
