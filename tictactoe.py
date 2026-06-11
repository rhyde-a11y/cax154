import random

def display_board(board):
    """Prints the board in its current state."""
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    """Prompts the user for their move, validates it, and updates the board."""
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid input. Please choose a number between 1 and 9.")
                continue
            
            # Map the 1-9 number to row and column indices
            row = (move - 1) // 3
            col = (move - 1) % 3
            
            # Check if the square is already occupied
            if board[row][col] in ['X', 'O']:
                print("That square is already taken! Choose another one.")
                continue
                
            board[row][col] = 'O'
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")


def make_list_of_free_fields(board):
    """Returns a list of tuples containing (row, col) for all empty squares."""
    free_fields = []
    for r in range(3):
        for c in range(3):
            if board[r][c] not in ['X', 'O']:
                free_fields.append((r, c))
    return free_fields


def victory_for(board, sign):
    """Checks if the player with the given 'sign' ('X' or 'O') has won."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:  # Row i
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:  # Column i
            return True
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
        
    return False


def draw_move(board):
    """Chooses a random free field for the computer's move ('X')."""
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'


# --- Main Game Loop ---
def play_game():
    # Initialize the board with numbers 1 to 9
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Rule: The computer always makes the first move in the center (square 5)
    board[1][1] = 'X'
    display_board(board)
    
    while True:
        # 1. User's turn
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("You win! 🎉")
            break
            
        if not make_list_of_free_fields(board):
            print("It's a tie! 🤝")
            break
            
        # 2. Computer's turn
        print("Computer is making a move...")
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("The computer wins! 🤖")
            break
            
        if not make_list_of_free_fields(board):
            print("It's a tie! 🤝")
            break

# Start the game
if __name__ == "__main__":
    play_game()