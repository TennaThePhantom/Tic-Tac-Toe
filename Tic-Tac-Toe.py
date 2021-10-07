# tic tak toe game
# two player and vs ai mode
# different board sizes 3x3 4x4 5x5 7x7x 10x10 20x20 30x30
# with user interface
# start menu another menu that shows the rules
# menu ask for 2 player or ai and asks you want board size you want to play on 
# can enter player 1 and player 2 name
# X and O maybe other symbols like custom symbols for each player if it's two player
# 
board = [" " for amount_of_spots in range(1, 9 + 1)]
def Tic_Tac_Toe_Board():
    print("\n")
    print("       |           | ")
    print("   " + board[1] + "   |     " + board[2] + "     |   " +  board[3])
    print("_______|___________|_______")
    print("       |           |")
    print("       |           |")
    print("_______|___________|_______")
    print("       |           | ")
    print("       |           | ")
    print("       |           | ")

    


print(Tic_Tac_Toe_Board())