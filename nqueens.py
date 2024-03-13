"""
Nqueens as a CSP
Author: Arsalan Bin Najeeb

"""

import numpy as np
from datetime import datetime
from queue import PriorityQueue


# read & create board with queens
board = np.zeros((30, 30), dtype=int)
n = board.shape[0]
np.set_printoptions(linewidth=2000)

rows_dont = []
queens_list = []


###################HELPERS######################


# Helper function for unittest cases, returns all (x,_) and (_,y) of queens placed in []'s
def get_all_queen_x_y(board):
    x_cord_queens = []
    y_cord_queens = []

    for idx, xy in np.ndenumerate(board):
        if xy == 1:
            x_cord_queens.append(idx[0])
            y_cord_queens.append(idx[1])

    return [x_cord_queens, y_cord_queens]


# Helper function to create a txt file with a nqueen true board
def print_sol(board):
    board[board == 8] = 0
    np.savetxt("sol" + str(n) + ".txt", board.copy(), fmt="%i")


######################################################


# Checks if placed queen on the board is in postion to attack any other queen + also implements a version of forward checking where I mark places on the board that are being attacked
def check_no_attack(queen):
    x, y = queen

    if board[x][y] == 1:
        return False

    # check col for other queens |
    x_q_count = 0
    for col in board[:, y]:
        if col == 1:
            x_q_count += 1
    if x_q_count >= 1:
        return False

    # check upper diagoanls \/
    up_l = y - 1
    up_r = y + 1
    i = x - 1
    while i >= 0:
        if up_l >= 0:
            if board[i][up_l] == 1:
                return False
            board[i][up_l] = 8

        if up_r < n:
            if board[i][up_r] == 1:
                return False
            board[i][up_r] = 8

        i = i - 1
        up_l = up_l - 1
        up_r = up_r + 1

    # check lower diagnols /\
    dn_l = y - 1
    dn_r = y + 1
    i = x + 1
    while i < n:
        if dn_l >= 0:
            if board[i][dn_l] == 1:
                return False
            board[i][dn_l] = 8

        if dn_r < n:
            if board[i][dn_r] == 1:
                return False
            board[i][dn_r] = 8

        i = i + 1
        dn_l = dn_l - 1
        dn_r = dn_r + 1

    for idx in np.ndenumerate(board[:, y]):
        board[idx[0][0]][y] = 8
    return True


# Minimum remaining value ordering heuristic, the next row to visit is the one with the least amount of safe space available for placing a queen
def mrv_row(board):
    temp_board = board.copy()

    max_fights = np.sum(temp_board == 8, axis=1)
    rd_nump = np.array(rows_dont)

    val_max = -1
    idx_max = -1
    for idx, x in np.ndenumerate(max_fights):
        if idx not in rd_nump:
            if x > val_max:
                val_max = x
                idx_max = idx[0]

    return idx_max


# Backtracking Search with all heuristics and ordering
def csp_search(board, row_idx):

    if n <= 3:
        print("No Solution")
        return False

    if row_idx == -1:
        print_sol(board.copy())
        get_all_queen_x_y(board.copy())
        return True

    # bt+mrv, next row chosen is the one with the least amount of cols left safe for placement(the fewest legal values(spaces) left for the variable(row))
    for idx, j in np.ndenumerate(board[row_idx]):
        if check_no_attack((row_idx,) + idx) == True:

            board[row_idx][idx] = 1
            rows_dont.append(row_idx)
            # MRV implementation
            mrr = mrv_row(board)

            if csp_search(board, mrr):
                return True

            rows_dont.remove(row_idx)
            board[row_idx][idx] = 0

    return False


# AC3 implementation is not complete
# def ac_3():
#     # go thorugh queen no attack constraints and check them
#     # if they dont hold remove them and backtrack since no values left for the variable(row wise)
#     unplaced_queens_queue = PriorityQueue()
#     unplaced_queens = []
#     for x in range(n):
#         if x not in queens_list:
#             print(x)
#             unplaced_queens_queue.put(x)
#             unplaced_queens.append(x)

#     while not unplaced_queens_queue.empty():
#         x = unplaced_queens_queue.get()
#         # the constraints are between each unplaced queens so have to look at all unplaced queens
#         for y in unplaced_queens:
#             if x != y:
#                 ac3_revise_helper(x, y)


# def ac3_revise_helper(x, y):
#     domain_reduced = False
#     for col in range(n):

#     print()


start_time = datetime.now()
csp_search(board, 0)
end_time = datetime.now()
print((end_time - start_time).microseconds)


# Runtimes
# 326796 ms with bt and mrv on 25n
# 2841 ms with bt and mrv on 10n
# 522287 ms with bt and mrv on 100n

# 443227 with just backtracking on 25n
# 1435 with just bt on 10n
