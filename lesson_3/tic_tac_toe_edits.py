import os
import random

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 2


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
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
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
    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def play_tic_tac_toe():
    computer_wins = 0
    human_wins = 0
    win_track = ''
    tie_track = ''

    while human_wins < GAMES_TO_WIN and computer_wins < GAMES_TO_WIN:
        board = initialize_board()

        while True:
            display_board(board)
            
            if tie_track:
                prompt(tie_track)
                prompt(f'Player wins = {human_wins}, Computer wins = {computer_wins}')
            elif win_track:
                prompt(f"{win_track} won this round!")
                prompt(f'Player wins = {human_wins}, Computer wins = {computer_wins}')
            else:
                prompt(f"Welcome to Tic Tac Toe! It is first to {GAMES_TO_WIN} wins!")
            
            tie_track = ''

            player_chooses_square(board)

            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break

        if someone_won(board):
            
            if detect_winner(board) == 'Player':
                human_wins += 1
                win_track = detect_winner(board)
            else:
                computer_wins += 1
                win_track = detect_winner(board)
        else:
            tie_track = "It's a tie!"

        # prompt("Play again? (y or n)")
        # answer = input().lower()[0]

        # if answer != 'y':
        #     break
        prompt(f"{detect_winner(board)} won!")
        prompt('Thanks for playing Tic Tac Toe!')

# Call the main game function
play_tic_tac_toe()