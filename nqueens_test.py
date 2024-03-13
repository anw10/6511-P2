import unittest
import nqueens


class TestNqueens(unittest.TestCase):

    def test_x_distinct(self):
        nqueens
        temp_board = nqueens.board
        x_cords = nqueens.get_all_queen_x_y(temp_board)[0]
        self.assertTrue(len(x_cords) == len(set(x_cords)))

    def test_y_distinct(self):
        nqueens
        temp_board = nqueens.board
        y_cords = nqueens.get_all_queen_x_y(temp_board)[1]
        self.assertTrue(len(y_cords) == len(set(y_cords)))

    def test_n_queens(self):
        nqueens
        n = nqueens.n
        temp_board = nqueens.board
        x_cords, y_cords = nqueens.get_all_queen_x_y(temp_board)
        self.assertTrue(len(x_cords) and len(y_cords) == n)


if __name__ == "__main__":
    unittest.main()
