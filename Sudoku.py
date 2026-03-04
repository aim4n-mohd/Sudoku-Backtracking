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
    row_arr = []
    col_arr = []
    
    for i in range(6):
        if board[i][col] not in row_arr:
            row_arr.append(board[i][col])
        else:
            return False
        
        if board[row][i] not in col_arr:
            if board[row][i] not in col_arr:
                col_arr.append(board[row][i])
            else:
                return False

    return True

def check_board(board):

    col_arr = []
    row_arr = []
    
    for i in range(9):
        for j in range(9):
            if board[i][j] not in row_arr:
                row_arr.append(board[i][j])
            else:
                return False
            
            if board[j][i] not in col_arr:
                col_arr.append(board[j][i])
            else:
                return False

    for row in range(0,9,3):
        for col in range(0,9,3):
            group_arr = []

            for r in range(row,row+3):
                for c in range(col,col+3):
                    if board[r][c] not in group_arr:
                        group_arr.append(board[r][c])
                    else:
                        return False
                    
    return True