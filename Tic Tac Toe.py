import random

def display_board(board):
    print('\n'*100)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    marker =' '
    while marker !='X' and marker!='O' :
        marker = input('Player 1 enter your marker:\n')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1,player2)


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark))

def choose_first():
    if random.randint(0,1) == 0 :
        return 'player 2'
    else :
        return 'player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(the_baord):
    for i in range(1,10):
        if space_check(the_board,i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) \n'))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: \n').lower().startswith('y')


print('Welcome to Tic Tac Toe')
while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+ ' will go first')
    game_on = False
    play_game = ' '
    while not game_on:
        play_game = input('Are you ready to play game? Yes or No.\n')
        if play_game.lower().startswith('y'):
            game_on = True
            break
        elif play_game.lower().startswith('n'):
            game_on = False
            break
        else:
            print('Select correct option : Yes or No\n')
    while game_on:
        if turn == 'player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congratulations, Player 1 has won!\n')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The Game has draw!\n')
                    break
                else:
                    turn = 'player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Congratulations, Player 2 has won!\n')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The Game has draw\n')
                    break
                else:
                    turn = 'player 1'
    if not replay():
        break



