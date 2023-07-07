def solve_sudoku(board):
    if is_board_valid(board):
        empty_cell = find_empty_cell(board)
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if is_valid_move(board, num, row, col):
                board[row][col] = num

                if solve_sudoku(board):
                    return True

                board[row][col] = 0

    return False

def is_board_valid(board):
    for i in range(9):
        if not is_row_valid(board, i) or not is_column_valid(board, i) or not is_subgrid_valid(board, i):
            return False
    return True

def is_row_valid(board, row):
    nums = set()
    for col in range(9):
        if board[row][col] != 0:
            if board[row][col] in nums:
                return False
            nums.add(board[row][col])
    return True

def is_column_valid(board, col):
    nums = set()
    for row in range(9):
        if board[row][col] != 0:
            if board[row][col] in nums:
                return False
            nums.add(board[row][col])
    return True

def is_subgrid_valid(board, subgrid):
    nums = set()
    start_row = (subgrid // 3) * 3
    start_col = (subgrid % 3) * 3
    for row in range(start_row, start_row + 3):
        for col in range(start_col, start_col + 3):
            if board[row][col] != 0:
                if board[row][col] in nums:
                    return False
                nums.add(board[row][col])
    return True

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_valid_move(board, num, row, col):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
            if j == 2 or j == 5:
                print("|", end=" ")
        print()
        if i == 2 or i == 5:
            print("- - - - - - - - - - - - - -")

def main():
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    if solve_sudoku(board):
        print("Sudoku solution:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()