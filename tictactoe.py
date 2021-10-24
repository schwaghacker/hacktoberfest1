import random

player_choice = 0
cpu_choice = 0
player_piece = "X"
ai_piece = "O"
play_again = True


def Player_Piece_Choice():
    choice = 0
    while True:
        choice = input("Please choose 1 for X or 2 for O. ")
        if choice == "1":
            player_piece = "X"
            ai_piece = "O"
            break
        elif choice == "2":
            player_piece = "O"
            ai_piece = "X"
            break


def safe_selection(board, loc):
    if board[loc] != " ":
        return True

    print("False")
    return False


def Print_Board(board):
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


def Print_Board_Start():
    print(str(1) + " | " + str(2) + " | " + str(3))
    print(str(4) + " | " + str(5) + " | " + str(6))
    print(str(7) + " | " + str(8) + " | " + str(9))


def Make_Selection(board):
    run = True
    while run:
        value = input("Please choose your location")
        run = safe_selection(board, int(value))

    board[int(value)] = player_piece


def Check_for_Win(board):
    if board[1] == board[2] == board[3] != " ":
        if board[1] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[4] == board[5] == board[6] != " ":
        if board[4] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[7] == board[8] == board[9] != " ":
        if board[7] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[1] == board[5] == board[9] != " ":
        if board[1] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[3] == board[5] == board[7] != " ":
        if board[3] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[1] == board[4] == board[7] != " ":
        if board[1] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[2] == board[5] == board[8] != " ":
        if board[2] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif board[3] == board[6] == board[9] != " ":
        if board[3] == player_piece:
            return "The player has won."
        else:
            return "The AI has won."
    elif " " not in board.values():
        return "Stalemate"
    else:
        return "inprog"


def AI_choice_dum(board):
    while True:
        ai_choice = random.randint(1, 9)

        if board[ai_choice] == " ":
            board[ai_choice] = ai_piece
            print(ai_choice)
            break


while play_again == True:
    board = {
        1: " ",
        2: " ",
        3: " ",
        4: " ",
        5: " ",
        6: " ",
        7: " ",
        8: " ",
        9: " "
    }

    Player_Piece_Choice()

    Print_Board_Start()

    while True:
        Make_Selection(board)
        Print_Board(board)
        winner_check = Check_for_Win(board)
        if winner_check != "inprog":
            print(winner_check)
            break

        AI_choice_dum(board)
        winner_check = Check_for_Win(board)
        Print_Board(board)
        if winner_check != "inprog":
            print(winner_check)
            break

    if input("Will you play again?- ") != "y":
        play_again == False
    else:
        play_again == True
