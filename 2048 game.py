import random

# Initialize the game board
def initialize_board():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Add a new tile (either 2 or 4) to a random empty cell
def add_new_tile(board):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = random.choice([2, 4])

# Check if the game is over (no more moves possible)
def game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return False
            if i < 3 and board[i][j] == board[i + 1][j]:
                return False
            if j < 3 and board[i][j] == board[i][j + 1]:
                return False
    return True

# Perform a move (left, right, up, or down)
def move(board, direction):
    def merge(row):
        merged_row = [0] * 4
        j = 0
        for i in range(4):
            if row[i] != 0:
                if merged_row[j] == 0:
                    merged_row[j] = row[i]
                elif merged_row[j] == row[i]:
                    merged_row[j] *= 2
                    j += 1
                else:
                    j += 1
                    merged_row[j] = row[i]
        return merged_row

    if direction == 'left':
        for i in range(4):
            board[i] = merge(board[i])
    elif direction == 'right':
        for i in range(4):
            board[i] = merge(board[i][::-1])[::-1]
    elif direction == 'up':
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            merged_column = merge(column)
            for i in range(4):
                board[i][j] = merged_column[i]
    elif direction == 'down':
        for j in range(4):
            column = [board[i][j] for i in range(4)]
            merged_column = merge(column[::-1])[::-1]
            for i in range(4):
                board[i][j] = merged_column[i]

# Print the game board
def print_board(board):
    for row in board:
        print(' '.join(str(cell).rjust(4) for cell in row))
    print()

# Main game loop
def play_game():
    board = initialize_board()
    print_board(board)

    while not game_over(board):
        direction = input("Enter move (left, right, up, down): ")
        move(board, direction)
        add_new_tile(board)
        print_board(board)

    print("Game over!")

if __name__ == "__main__":
    play_game()
