import numpy as np
from datetime import datetime


#read & create board with queens
board = np.zeros((25,25),dtype=int)
n = board.shape[0]
np.set_printoptions(linewidth=200)

rows_dont=[]

# r_idx = 0
# with open("n-queen.txt") as mfile:
#     for line in mfile:
#         if not (line[0] == '#'):
#             board[r_idx][int(line.rstrip())-1] = 1
#             r_idx += 1
# sol_board = np.zeros((10,10),dtype=int)

def check_no_attack(queen):
    x,y = queen

    if(board[x][y] == 1):
        return False

    
    #check col for other queens
    x_q_count = 0
    for col in board[:,y]:
        if col == 1:
            x_q_count += 1
    if x_q_count >= 1:
        return False
        

    #check upper diagoanls         
    up_l = y-1
    up_r = y+1
    i = x-1
    while i >= 0:
        if(up_l >= 0):
            if(board[i][up_l] == 1):
                return False
            board[i][up_l] = 8

        if(up_r < n):
            if(board[i][up_r] == 1):
                return False
            board[i][up_r] = 8    

        i = i-1
        up_l = up_l-1
        up_r = up_r+1

    #check lower diagnols
    dn_l=y-1    
    dn_r = y+1
    i = x+1
    while i < n:
        if(dn_l >= 0):
            if(board[i][dn_l] == 1):
                return False
            board[i][dn_l] = 8
        
        if(dn_r < n):
            if(board[i][dn_r] == 1):
                return False
            board[i][dn_r] = 8
        
        i = i+1
        dn_l = dn_l-1
        dn_r = dn_r+1

    for idx in np.ndenumerate(board[:,y]):
            board[idx[0][0]][y] = 8
    return True 


def csp_search(board, row_idx):

    if row_idx == -1:
        print(board.copy(), "FINAL")
        return True
    
    #just go top down row by row bt
    for idx, j in np.ndenumerate(board[row_idx]):
        if(check_no_attack((row_idx,) + idx) == True):
            board[row_idx][idx] = 1
            rows_dont.append(row_idx)
            # print(board)
            # print(row_idx)
            mrr = mrv_row(board)

            if(csp_search(board, mrr)):
                return True

            board[row_idx][idx] = 0            
    
    return False

def mrv_row(board):
    temp_board = board.copy()
    # print((temp_board == 8).sum(axis=1))
    max_fights = np.sum(temp_board == 8, axis=1)
    rd_nump = np.array(rows_dont)
    # print(max_fights)
    # print(rd_nump)

    val_max = -1
    idx_max = -1
    for idx,x in np.ndenumerate(max_fights):
        if(idx not in rd_nump):
            if(x > val_max):
                val_max = x
                idx_max = idx[0]
    
    return idx_max
 


def heu_cal():
    print()

def ac_3():
    print()


start_time = datetime.now()
csp_search(board, 0)
end_time = datetime.now()
print((end_time-start_time).microseconds)

#443227 with just backtracking on 25n
#1435 with just bt on 10n

#4962 with bt and mrv on 25n
#641 with bt and mrv on 10n