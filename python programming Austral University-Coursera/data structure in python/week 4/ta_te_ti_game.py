"""
program the TA-TE-TI game. 
When the program starts to run, the screen shows the TA-TE-TI board (3x3) 
and an input that allows the user to choose the “X” symbol or the “O” symbol. 
The "Xs" begin.

The user must choose the position of the board (this position must be correct and 
must not be occupied) where to put the symbol on the board and the system validates
if the game ends with a winner or a draw. If there is no winner or 
the game has not yet ended in a tie, the game continues by asking the other user 
to select the position on the board where he wants to put his symbol and so on 
until the game ends with a winner or in a tie.

Notes:
* Represent the board as a 3x3 matrix.
* The game ends in a draw when the board is complete and there are no winners.
* Empty board drawing example:

| _ | _ | _ |

| _ | _ | _ |

| _ | _ | _ |

Example of full board screen drawing:

| X | X | O |

| O | O | X |

| X | X | O |"""


# board printing 
def print_board(board):
    for row in board:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i], end='\n')
            else:
                print(row[i], end='  ')

#change player turn
def change_board(board, position, player):
    if player:
        symbol = 'x'
    else:
        symbol = 'o'
    
    if position == 1:
        if board[4][0] == ' ':
            board[4][0] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 2:
        if board[4][2] == ' ':
            board[4][2] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 3:
        if board[4][4] == ' ':
            board[4][4] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 4:
        if board[2][0] == ' ':
            board[2][0] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 5:
        if board[2][2] == ' ':
            board[2][2] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 6:
        if board[2][4] == ' ':
            board[2][4] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 7:
        if board[0][0] == ' ':
            board[0][0] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 8:
        if board[0][2] == ' ':
            board[0][2] = symbol
            return 0
        else:
            return 'position occupy.'
    elif position == 9:
        if board[0][4] == ' ':
            board[0][4] = symbol
            return 0
        else:
            return 'position occupy.'
    else:
        return 'position does not exist.'

# there is a winner in the game
def thereis_winner(board):
    for symbol in ['x', 'o']:
        row_0 = board[0][0] == symbol and board[0][2] == symbol and board[0][4] == symbol
        row_2 = board[2][0] == symbol and board[2][2] == symbol and board[2][4] == symbol
        row_4 = board[4][0] == symbol and board[4][2] == symbol and board[4][4] == symbol
        column_0 = board[0][0] == symbol and board[2][0] == symbol and board[4][0] == symbol
        column_2 = board[0][2] == symbol and board[2][2] == symbol and board[4][2] == symbol
        column_4 = board[0][4] == symbol and board[2][4] == symbol and board[4][4] == symbol
        diagonal_bottom = board[0][0] == symbol and board[2][2] == symbol and board[4][4] == symbol
        diagonal_top = board[4][0] == symbol and board[2][2] == symbol and board[0][4] == symbol

        if row_0 or row_2 or row_4 or column_0 or column_2 or column_4 or diagonal_bottom or diagonal_top:
            if symbol == 'x':
                return 1
            elif symbol == 'o':
                return 2
            break

#board drawing
board = [
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' '],
    ['-', '+', '-', '+', '-'],
    [' ', '|', ' ', '|', ' ']
]
turn_1 = True
player_1 = ''
player_2 = ''
turn = 0
#board printin after play
print_board(board)
while turn < 9:
    if player_1 == '':
        print('player name 1 (x)')
        player_1 = input()
        print('player name 2 (o)')
        player_2 = input()
    else:
        if turn_1:
            print(player_1 + ', choose a position')
        else:
            print(player_2 + ', choose a position')
        
        jugada = int(input())

        value = change_board(board, jugada, turn_1)
        if value == 0:
            turn_1 = not turn_1
            turn += 1
            print_board(board)
            if thereis_winner(board) == 1:
                print(player_1 + " won!")
                break
            elif thereis_winner(board) == 2:
                print(player_2 + " won!")
                break
        else:
            print(value)
        
        if turn == 9:
            print("tie...")
