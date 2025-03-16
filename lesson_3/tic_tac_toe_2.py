import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAME_COUNT = 5
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
CHOOSE_FIRST_UP = ['Player', 'Computer']

def join_or(lst, sep=', ', end='or'):
    final_string = ''
    
    for indx, num in enumerate(lst):
        if len(lst) == 1:
            final_string += str(num)
        elif len(lst) > 2 and indx != (len(lst) - 1):
            final_string += str(num) + sep
        elif len(lst) == 2 and indx != (len(lst) - 1):
            final_string += str(num) + ' '
        else:
            final_string += end + ' ' + str(num)
    return final_string

def prompt(message):
    print(f"==> {message}")

def display_board(board):
    os.system('clear')
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'

    return None

def someone_won(board):
    return bool(detect_winner(board))

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
            return
    
    square = None

    for line in WINNING_LINES:
            square = find_at_risk_square(line, board, COMPUTER_MARKER)
            if square:
                break
    
    if not square:
        for line in WINNING_LINES:
            square = find_at_risk_square(line, board, HUMAN_MARKER)
            if square:
                break
          
    if not square:
        if 5 in empty_squares(board):
            square = 5

    if not square:
        square = random.choice(empty_squares(board))

    board[square] = COMPUTER_MARKER

def win_status(player, computer):
    prompt(f'Player has {player} wins \n Computer has {computer} wins')

def find_at_risk_square(line, board, marker):
    markers_in_line = [board[square] for square in line]

    if markers_in_line.count(marker) == 2:
        for square in line:
            if board[square] == INITIAL_MARKER:
                return square
    return None

def play_tic_tac_toe():

    while True:        

        prompt(f"Welcome to Tic Tac Toe!\n First to {GAME_COUNT} wins!")
        prompt(f'Ready to play? (y/n)')

        play_status = input().lower()

        if play_status and play_status[0] != 'y':
            break
        
        prompt("Pick who is going first (Type: '0' for Player, Type: '1' for Computer)")
        first_up = int(input())

        player_wins = 0
        computer_wins = 0

        while player_wins < GAME_COUNT and computer_wins < GAME_COUNT:

            board = initialize_board()

            while True:
                display_board(board)

                win_status(player_wins, computer_wins)

                if CHOOSE_FIRST_UP[first_up] == 'Player':
                    player_chooses_square(board)
                    if someone_won(board) or board_full(board):
                        break

                    computer_chooses_square(board)
                    if someone_won(board) or board_full(board):
                        break
                else:
                    computer_chooses_square(board)
                    display_board(board)
                    if someone_won(board) or board_full(board):
                        break

                    player_chooses_square(board)
                    if someone_won(board) or board_full(board):
                        break

            if someone_won(board):
                display_board(board)
                prompt(f"{detect_winner(board)} won this round!")
                if detect_winner(board) == 'Player':
                    player_wins += 1
                else:
                    computer_wins += 1
                input('Press enter to continue!')
            else:
                display_board(board)
                prompt("It's a tie!")
                input('Press enter to continue!')
        
        if player_wins == GAME_COUNT:
            prompt("You Win!")
        else:
            prompt("You Lose!")
            

        prompt("Play again? (y or n)")
        answer = input().lower()
        if answer not in ['y', 'yes', 'no', 'n']:
            prompt("Play again? (y or n)")
            answer = input().lower()
        elif answer == 'y' or answer == 'yes':
            continue
        elif answer == 'n' or answer == 'no':    
            break
       
    prompt('Thanks for playing Tic Tac Toe!')

# Call the main game function
play_tic_tac_toe()