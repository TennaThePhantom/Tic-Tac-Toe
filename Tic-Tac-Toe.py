# tic tak toe game
# two player and vs ai mode
# different board sizes 3x3 4x4 5x5 7x7x 10x10 20x20 30x30
# with user interface
# start menu another menu that shows the rules
# menu ask for 2 player or ai and asks you want board size you want to play on 
# can enter player 1 and player 2 name
# X and O maybe other symbols like custom symbols for each player if it's two player
# 
board = [" " for amount_of_spots in range(10)]
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

