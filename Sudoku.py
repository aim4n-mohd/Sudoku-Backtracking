import time

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
            if board[i][j]!=0:
                if board[i][j] not in group_arr:
                    group_arr.append(board[i][j])
                else:
                    return False

    return True

def check_board(board):
    #2 loops for each col of each row
    for i in range(9):
        #Initialize arrays for each iteration or row/col
        col_arr = []
        row_arr = []
        for j in range(9):
            #checking for any zeroes
            if board[i][j] == 0:
                return False
            
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


def solve(board, row, col):
    if row == 9:
        return True
    if board[row][col]: #skips the cells with existing/unchangeable values
        next_row = row + (col//8)
        next_col = (col+1) % 9
        return solve(board, next_row, next_col)
    else:
        for num in range(1,10):
            board[row][col] = num
            if cell_check(board, row, col):
                if solve(board, row+(col//8), (col+1)%9):
                    return True
        board[row][col] = 0
        return False
            

board = []
print("Enter values row by row: ")
for i in range(9):
    #   row = list(map(int, input().split()))
    row = []
    row_inp = input()
    for j in row_inp:
        if j in ("1234567890"):
            row.append(int(j))
    board.append(row)

solved = solve(board, 0, 0)

start = time.time()

if solved:
    print("\n\nSolution:\n")
    for i in board:
        print(i)
else:
    print("\n\nSOLUTION NOT POSSIBLE!!!")

end = time.time()
print(f"Time Taken - {end-start}")

