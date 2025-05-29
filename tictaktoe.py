import random

# Define the game board
def create_board():
    return [" " for _ in range(9)]

# Display the board
def print_board(board):
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Check if a player has won
def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

# Check if the game is a tie
def check_tie(board):
    return all(cell != " " for cell in board)

# AI move - simple random strategy
def ai_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]
    return random.choice(available_moves)

# Main game loop
def play_game():
    board = create_board()
    current_player = "X"  # Human starts, AI is "O"

    while True:
        print_board(board)

        if current_player == "X":
            move = int(input("Enter your move (0-8): "))
            if board[move] != " ":
                print("Invalid move. Try again.")
                continue
        else:
            move = ai_move(board)
            print(f"AI chooses position {move}")

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

# Call the main game loop
if __name__ == "__main__":
    play_game()
