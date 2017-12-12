from random import *
import time

game_on = True

def init_board():
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9] # pylint: disable=invalid-name

def player_names():
    """
    Asks players for their names and sets them to global variables
    """
    global player1_name 
    player1_name = input(" Player one, what is your name? \n>>> ")
    global player2_name
    player2_name = input(" Player two, what is your name? \n>>> ")

def who_goes_first(p1, p2):
    """
    Accepts two names, generates two random numbers, and compares these to decide who goes first
    """
    global first
    global second
    global player_turn
    rand = randint(1, 100)
    if rand % 2 == 0:
        first = p1
        second = p2
        player_turn = p1
    else:
        first = p2
        second = p1
        player_turn = p2



def display_board(board):
    """
    Takes a list and outputs that list into a tic-tac-toe board
    """
    print("  " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))
    print(" ------------")
    print("  " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print(" ------------")
    print("  " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))

def xo_check():
    """
    INPUT: X or O, name of the player that goes first
    OUTPUT: Assigns input letter to the player that goes first
    """
    global player1_letter
    global player2_letter
    global player_letter
    while True:
        player_letter = str(input(">>> "))
        player_letter = player_letter.capitalize()
        if player_letter == "X" or player_letter == "O":
            if player1_name == first:
                if player_letter == "X":
                    player2_letter = "O"
                    player1_letter = "X"
                    break
                else:
                    player1_letter = "O"
                    player2_letter = "X"
                    break
            else:
                if player_letter == "X":
                    player2_letter = "X"
                    player1_letter = "O"
                    break
                else:
                    player1_letter = "X"
                    player2_letter = "O"
                    break
        else:
            print(" You seem to have entered something other than an 'X' or an 'O'... try again!")
            print(" Please choose if you would like to be 'X' or 'O': ")


def place_marker(in_board, marker, position):
    global board
    board[position] = marker


def replay():
    print(" Would you like to setup another game? [Type Yes/No]")
    new_game = input(">>> ")
    new_game = new_game.lower()
    if new_game[0] == "n":
        return False
    return True


def win_check(board, mark):
    """
    Checks if someone wins
    """
    if mark == board[0] and mark == board[1] and mark == board[2]:
        return True
    elif mark == board[0] and mark == board[3] and mark == board[6]:
        return True
    elif mark == board[0] and mark == board[4] and mark == board[8]:
        return True
    elif mark == board[1] and mark == board[4] and mark == board[7]:
        return True
    elif mark == board[2] and mark == board[5] and mark == board[8]:
        return True
    elif mark == board[2] and mark == board[4] and mark == board[6]:
        return True
    elif mark == board[3] and mark == board[4] and mark == board[5]:
        return True
    elif mark == board[6] and mark == board[7] and mark == board[8]:
        return True
    return False

def is_draw(board):
    """
    Checks if the board is full
    """
    count = 0
    for spot in range(0, 9):
        if isinstance(board[spot], int):
            count += 1
    if count == 0:
        return True
    return False

def space_check(in_board, position):
    """
    Checks if a position on a board is already occupied
    """
    if isinstance(in_board[position], int):
        return False
    return True

def player_input(player):
    """
    Asks player where their next move will be
    """
    global board
    while True:
        print(" Enter the number for the box you'd like to take...")
        next_move = int(input(">>> "))
        next_move -= 1
        check = space_check(board, next_move)

        if not check:
            print(check)
            if player == player1_name:
                board[next_move] = player1_letter
                break
            else:
                board[next_move] = player2_letter
                break
        else:
            print(" Sorry, that space is occupied!")
            display_board(board)




# Now run the game
while True:
    print(' Welcome to Tic Tac Toe!')

    player_names()

    print(" Great! Rolling the die to see who goes first...")

    time.sleep(1)

    who_goes_first(player1_name, player2_name)

    print(" Okay, " + first + " you will go first this time.")

    time.sleep(1)

    print(" Since you're first, please choose if you would like to be 'X' or 'O':")

    xo_check()

    print(" Alright! " + first + " is going first and is playing as " + player_letter + "\n")

    time.sleep(1)

    init_board()

    display_board(board)

    time.sleep(1)

    while game_on:

        #Player 1 Turn
        while player_turn == player1_name:
            print(" It's " + player1_name + "'s turn now.")
            player_input(player1_name)

            if win_check(board, player1_letter):
                game_on = False
                display_board(board)
                print(" Yay!!! " + player1_name + " wins!!!")
                break

            if is_draw(board):
                game_on = False
                display_board(board)
                print(" The game has ended in a draw!")
                break

            display_board(board)


            player_turn = player2_name
        
        # Player2's turn.
        while player_turn == player2_name:
            print(" It's " + player2_name + "'s turn now.")
            player_input(player2_name)

            if win_check(board, player2_letter):
                game_on = False
                display_board(board)
                print(" Yay!!! " + player2_name + " wins!!!")
                break

            if is_draw(board):
                game_on = False
                display_board(board)
                print(" The game has ended in a draw!")
                break

            display_board(board)


            player_turn = player1_name

    if not replay():
        print(" Thanks for playing!")
        break
    else:
        game_on = True
