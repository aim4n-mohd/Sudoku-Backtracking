board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

def cell_check(board, row, col):
    #initialize arrays for keeping track of nums
    row_arr = []
    col_arr = []
    group_arr = []
    
    for i in range(9):
        #check row
        if board[row][i]!=0:
            if (board[row][i] not in row_arr):
                row_arr.append(board[row][i])
            else:
                return False
        #check column
        if board[i][col]!=0:
            if board[i][col] not in col_arr:
                col_arr.append(board[i][col])
            else:
                return False

    #get top left corner value of element group
    start_row = (row//3) * 3
    start_col = (col//3) * 3
    #check group, starting from top left 
    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if board[i][j] not in group_arr:
                group_arr.append(board[i][j])
            else:
                return False

    return True

def check_board(board):
    #initialize arrays to track
    col_arr = []
    row_arr = []
    #2 loops for each col of each row
    for i in range(9):
        for j in range(9):
            #checking rows
            if board[i][j] not in row_arr:
                row_arr.append(board[i][j])
            else:
                return False
            #checking cols
            if board[j][i] not in col_arr:
                col_arr.append(board[j][i])
            else:
                return False
    #outer loop with step=3 to get the start of each group
    for row in range(0,9,3):
        for col in range(0,9,3):
            group_arr = []
            #inner loop runs only 3 times per outer loop, for each element in group
            for r in range(row,row+3):
                for c in range(col,col+3):
                    #logic to check group
                    if board[r][c] not in group_arr:
                        group_arr.append(board[r][c])
                    else:
                        return False
                    
    return True