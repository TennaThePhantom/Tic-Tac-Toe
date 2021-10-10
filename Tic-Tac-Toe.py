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
    board[Letter] = Position

def IsTheBoxOpen(Position): # can you place a letter  
    return board[Position] == " "

def Winner(boardSpot, Letter): # how to win the game
    return (boardSpot[1] == Letter and boardSpot[2] == Letter and boardSpot[3] == Letter) or (
        boardSpot[4] == Letter and boardSpot[5] == Letter and boardSpot[6] == Letter
    ) or (
        boardSpot[7] == Letter and boardSpot[8] == Letter and boardSpot[9] == Letter
    ) or (boardSpot[1] == Letter and boardSpot[4] == Letter and boardSpot[7] == Letter) or(
        boardSpot[2] == Letter and boardSpot[5] == Letter and boardSpot[8] == Letter) or (
            boardSpot[3] == Letter and boardSpot[6] == Letter and boardSpot[9] == Letter) or (
                boardSpot[1] == Letter and boardSpot[5] == Letter and boardSpot[9] == Letter) or (
                    boardSpot[3] == Letter and boardSpot[5] == Letter and boardSpot[7] == Letter)

def IstheBoardFull(board):
    return ""


def randomMove():
    return ""

def playerMove():
    return ""

def player2Move():
    return ""

def AiMove():
    return ""


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
    print("Hello " + player1 + " and " + player2)
    print(Tic_Tac_Toe_Board())



if Two_player == False and Ai == True:
    player1 = input("Enter your name ").upper()
    Ai_name = random.choice(List_of_ai_names)
    print(Ai_name)
    print(Tic_Tac_Toe_Board())
    while Two_player == False and Ai == True:
        while not (IstheBoardFull(board)):
 
            if IstheBoardFull(board):
                print("Tie Game ")
