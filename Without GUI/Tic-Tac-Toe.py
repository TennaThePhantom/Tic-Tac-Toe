# tic tak toe game
# two player and vs ai mode
# different board sizes 3x3 4x4 5x5 7x7x 10x10 20x20 30x30
# with user interface
# start menu another menu that shows the rules
# menu ask for 2 player or ai and asks you want board size you want to play on 
# can enter player 1 and player 2 name
# X and O maybe other symbols like custom symbols for each player if it's two player
# 
import random

board = [" " for amount_of_spots in range(10)]
List_of_ai_names = ["Jerry", "Jackson", "Mike", "John", "Peter", "Stella", "Anna", "Mia"]
def Tic_Tac_Toe_Board():
    print("\n")
    print("       |           | ")
    print("   " + board[1] + "   |     " + board[2] + "     |   " +  board[3])
    print("_______|___________|_______")
    print("       |           |")
    print("   " + board[4] + "   |     " + board[5] + "     |   " +  board[6])
    print("_______|___________|_______")
    print("       |           | ")
    print("   " + board[7] + "   |     " + board[8] + "     |   " +  board[9])
    print("       |           | ")

def LetterInBox(Letter, Position ): # to place the letter on the board
    board[Position] = Letter

def IsTheBoxOpen(Position): # can you place a letter  
    return board[Position] == " "

def Winner(boardSpot, Letter): # how to win the game
    return (boardSpot[1] == Letter and boardSpot[2] == Letter and boardSpot[3] == Letter) or ( # first row
        boardSpot[4] == Letter and boardSpot[5] == Letter and boardSpot[6] == Letter) or ( # second row
        boardSpot[7] == Letter and boardSpot[8] == Letter and boardSpot[9] == Letter) or ( # third row
        boardSpot[1] == Letter and boardSpot[4] == Letter and boardSpot[7] == Letter) or ( # down first colum
        boardSpot[2] == Letter and boardSpot[5] == Letter and boardSpot[8] == Letter) or ( # down second colum
        boardSpot[3] == Letter and boardSpot[6] == Letter and boardSpot[9] == Letter) or ( # down third colum
        boardSpot[1] == Letter and boardSpot[5] == Letter and boardSpot[9] == Letter) or ( # diagonal
        boardSpot[3] == Letter and boardSpot[5] == Letter and boardSpot[7] == Letter) # diagonal

def IstheBoardFull(board): # if there is more than 1 empty space on the space it is not full
    if board.count(' ') > 1:
        return False
    else:
        return True


def randomMove(Board_spots): # picks random spot
    length = len(Board_spots)
    random_number = random.randrange(0, length)
    return Board_spots[random_number]


def playerMove(): # for the player to move on the board
    did_the_player_move = False
    while did_the_player_move == False:
        try:
            pick_spot_on_board = int(input("Please pick a position between 1 through 9 to place a X: "))
            if pick_spot_on_board in range(1,9 + 1):
                if IsTheBoxOpen(pick_spot_on_board):
                    did_the_player_move = True
                    LetterInBox("X", pick_spot_on_board)
                else:
                    print("Space is taken")
            else:
                print("Please type a number within the range!")
        except:
            print("Next time type a number! ")
        


def player2Move():
    did_the_player_move = False
    while did_the_player_move == False:
        try:
            pick_spot_on_board = int(input("Please pick a position between 1 through 9 to place a O: "))
            if pick_spot_on_board in range(1,9 + 1):
                if IsTheBoxOpen(pick_spot_on_board):
                    did_the_player_move = True
                    LetterInBox("O", pick_spot_on_board)
                else:
                    print("Space is taken")
            else:
                print("Please type a number within the range!")
        except:
            print("Next time type a number! ")
        

def AiMove():
    any_move_Possible = [The_spot_on_board for The_spot_on_board, letter in enumerate(board) if letter == ' ' and The_spot_on_board != 0]
    move = 0

    for letter in ['O', 'X']: # checks if x or o can win
        for spot in any_move_Possible: # looks at all emepty spaces on board
            boardCopy = board[:] # copy original board
            boardCopy[spot] = letter # places the letter at the emepty position it finds
            if Winner(boardCopy, letter): # can you place the letter and win it blocks player or goes there to win game
                move = spot # does the move
                return move
    open_Corners =  []
    for spot in any_move_Possible:
        if spot in [1,3,7,9]: # checks corners on board
            open_Corners.append(spot)
            
    if len(open_Corners) > 0: # can I place a letter on corner
        move = randomMove(open_Corners) # places letter
        return move


    if 5 in any_move_Possible: # middle of board
        move = 5
        return move

    Edges_Open = []
    for spot in any_move_Possible:
        if spot in [2,4,6,8]: # checks edges on board
            Edges_Open.append(spot)
    if len(Edges_Open) > 0: # can I place letter on edges
        move = randomMove(Edges_Open) # places letter
    
    return move

print("Welcome to Tic Tac Toe!")
Tic_tac_toe_has_Started = True
while Tic_tac_toe_has_Started == True:
    Ai = False
    Two_player = False
    Choose_between_2_player_or_Ai = input("Do you want to vs the Ai or Two player? ").lower()
    if Choose_between_2_player_or_Ai == "ai":
        Ai = True
        Two_player = False
        break
    elif Choose_between_2_player_or_Ai == "two player":
        Ai = False
        Two_player = True
        break
    else:
        print("I don't understand what you said. Please say ai or two player ")
    continue

if Two_player == True and Ai == False:
    player1 = input("Player 1 enter your name ").upper()
    player2 = input("player 2 enter your name ").upper()
    print(Tic_Tac_Toe_Board())
    print("Hello " + player1 + " and " + player2)
    who_goes_first = random.randint(1,2)
    if who_goes_first == 1:
        player1_goes_first = True
        print(player1 + " goes first ")
    else:
        player1_goes_first = False
        print(player2 + " goes first")
    while player1_goes_first == True:
        while not(IstheBoardFull(board)):
            if not(Winner(board, 'O')):
                playerMove()
                print(Tic_Tac_Toe_Board())
                print(player1 + " has went your turn " + player2)
            else:
                print("Sorry" + player1 + ". You have lost to " + player2)
                break

            if not(Winner(board, 'X')):
                if IstheBoardFull(board):
                    print("Tie Game")
                else:
                    player2Move()
                    print(Tic_Tac_Toe_Board())
                    print(player2 + " has went your turn " + player1)
            else:
                print("Sorry " + player2 + ". You have lost to " + player1)
                break
        break

    while player1_goes_first == False:
        while not(IstheBoardFull(board)):
            if not(Winner(board, 'O')):
                player2Move()
                print(Tic_Tac_Toe_Board())
                print(player2 + " has went your turn " + player1)
            else:
                print("Sorry" + player1 + ". You have lost to " + player2)
                break
            if not(Winner(board, 'X')):
                if IstheBoardFull(board):
                    print("Tie Game")
                else:
                    playerMove()
                    print(player1 + " has went your turn " + player2)
                    print(Tic_Tac_Toe_Board())
            else:
                print("Sorry " + player2 + ". You have lost to " + player1)
                break
        break

if Two_player == False and Ai == True:
    player1 = input("Enter your name ").upper()
    Ai_name = random.choice(List_of_ai_names)
    print(player1 + " You are facing " + Ai_name)
    print(Tic_Tac_Toe_Board())
    while Two_player == False and Ai == True:
        while not (IstheBoardFull(board)): # is the full board yes or no if no continue 
            if not(Winner(board, 'O')): # the board is not full but you lost to the ai 
                playerMove()
                print(Tic_Tac_Toe_Board())
            else:
                print("Sorry you have lost to " + Ai_name)
                break

            if not(Winner(board, 'X')): # the board is not full but you won against the ai
                computerMove = AiMove()
                if computerMove == 0:
                    print("Tie Game!")
                else:
                    LetterInBox('O',computerMove)
                    print(Ai_name + " has place his letter your turn!")
                    print(Tic_Tac_Toe_Board())
            else:
                print("Sorry " + Ai_name + " the player has won. Good Job player!")
                break
        break
