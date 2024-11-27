from random import randrange

def display_board(board):
    print("+-------" * 3 + "+", sep="")
    for row in range(3):
        print("|       " * 3 + "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3 + "|", sep="")
        print("+-------" * 3 + "+", sep="")

def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0] // 3][condition[0] % 3] == board[condition[1] // 3][condition[1] % 3] == board[condition[2] // 3][condition[2] % 3] and board[condition[0] // 3][condition[0] % 3] != ' ':
            return board[condition[0] // 3][condition[0] % 3]
    return None

def is_full(board):
    return all(not isinstance(cell, int) for row in board for cell in row)

def check_move(board, move):
    if move < 1 or move > 9:
        return False
    row = (move - 1) // 3
    col = (move - 1) % 3
    return isinstance(board[row][col], int)

def make_move(board, move, player):
    row = (move - 1) // 3
    col = (move - 1) % 3
    board[row][col] = player

def computer_move(board):
    while True:
        move = randrange(1, 10)
        if check_move(board, move):
            make_move(board, move, 'X')
            break

def game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    while True:
        display_board(board)
        try:
            move = int(input("Enter your move (1-9) or 0 to quit: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if move == 0:
            print("Goodbye!")
            break

        if check_move(board, move):
            make_move(board, move, 'O')
            winner = check_win(board)
            if winner:
                display_board(board)
                print("You won!")
                break
            elif is_full(board):
                display_board(board)
                print("It's a tie!")
                break

            computer_move(board)
            winner = check_win(board)
            if winner:
                display_board(board)
                print("Computer won!")
                break
            elif is_full(board):
                display_board(board)
                print("It's a tie!")
                break
        else:
            print("Invalid move, try again.")

game()