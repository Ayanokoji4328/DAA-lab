def is_safe(board, row, col): 
    for i in range(len(board)): 
        placed_row = board[i] 
        placed_col = i + 1 
        if abs(placed_row - row) == abs(placed_col - col): 
            return False  
    return True  
def solve(col, n, board, solutions, used): 
    if col > n: 
        solutions.append(board.copy()) 
        return 
    for row in range(1, n + 1): 
        if not used[row]: 
            if is_safe(board, row, col):  
                used[row] = True 
                board.append(row) 
                solve(col + 1, n, board, solutions, used)
                board.pop() 
                used[row] = False 
def n_queen(n): 
    solutions = [] 
    board = [] 
    used = [False] * (n + 1) 
    solve(1, n, board, solutions, used) 
    return solutions 
if __name__ == "__main__": 
    n = int(input("Enter the number of queens: ")) 
    solutions = n_queen(n) 
    if not solutions: 
        print("No solution possible") 
    else: 
        for solution in solutions: 
            print(solution) 
