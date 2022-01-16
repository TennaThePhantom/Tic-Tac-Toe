import pygame
import sys
from pygame.locals import *

pygame.init()

Board6X6_Height = 600
Board6X6_Width = 600
Lines_Width = 12
Board_Screen = pygame.display.set_mode((Board6X6_Width, Board6X6_Height))

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

Font = pygame.font.SysFont(None, 75)

Mouse_Clicked = False
Player = 1
Position = (0, 0)
Board = []
Game_Over = False
Winner = 0

for Boxes in range(6):
    Rows = [0] * 6
    Board.append(Rows)

""" Creates the [0, 0, 0, 0, 0, 0, 0] Instead of having me to hardcode it
have to be print(Board) first 
doesn't work if you called emepty_board First"""
def emepty_board(Board):
    for Boxes in range(6):
        Rows = [0] * 6
        Board.append(Rows)
    print(Board)

Play_Again_Box = Rect(Board6X6_Width // 2 - 130, Board6X6_Height // 2 + 25, 325, 75)

def draw_board():
    Background = WHITE
    Grid_Lines_Color = BLACK
    Board_Screen.fill(Background)
    for Grid_lines in range(1, 6):
        pygame.draw.line(Board_Screen, Grid_Lines_Color, (0, 100 * Grid_lines), (Board6X6_Width, 100 * Grid_lines), Lines_Width)
        pygame.draw.line(Board_Screen, Grid_Lines_Color, (100 * Grid_lines, 0), (100 * Grid_lines, Board6X6_Height), Lines_Width)


def draw_letter():
    X_Position = 0
    for Spots in Board:
        Y_Position = 0
        for Player in Spots:
            if Player == 1:
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 100 + 15, Y_Position * 100 + 15), (X_Position * 100 + 85, Y_Position * 100 + 85), Lines_Width)
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 100 + 15, Y_Position * 100 + 85), (X_Position * 100 + 85, Y_Position * 100 + 15), Lines_Width)
            if Player == -1:
                pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 100 + 50, Y_Position * 100 + 50), 40, Lines_Width)
            Y_Position += 1
        X_Position += 1


def draw_game_over_text(winner):
    if winner != 0:
        End_Text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        End_Text = "You have tied!"

    End_Img = Font.render(End_Text, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, (Board6X6_Width // 2 - 170, Board6X6_Height // 2 - 60, 390, 65))
    Board_Screen.blit(End_Img, (Board6X6_Width // 2 - 150, Board6X6_Height // 2 - 50))

    Play_Again = 'Play Again?'
    Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
    Board_Screen.blit(Play_Again_IMG, (Board6X6_Width // 2 - 120, Board6X6_Height // 2 + 40))


def how_to_win_colum():
    global Game_Over
    global Winner

    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True


def how_to_win_diagonal():
    global Game_Over
    global Winner

    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][0] + Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] + Board[0][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][0] + Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] + Board[0][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == -5:
        Winner = 2
        Game_Over = True


def is_the_game_over():
    global Game_Over
    global Winner
    how_to_win_colum()
    how_to_win_diagonal()

    Letter = 0
    for Spots in Board: 
        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == -5:
            Winner = 2
            Game_Over = True
        Letter += 1

    if Game_Over == False:
        Tie = True
        for Row in Board:
            for Zero in Row:
                if Zero == 0:
                    Tie = False
        if Tie == True:
            Game_Over = True
            Winner = 0


def start_6x6_board():
    global Winner
    global Game_Over
    global Position
    global Board
    global Player
    global Mouse_Clicked

    Start_Tic_Tac_Toe = True
    while Start_Tic_Tac_Toe == True:
        draw_board() 
        draw_letter()
        for Window in pygame.event.get():
            if Window.type == pygame.QUIT:
                Start_Tic_Tac_Toe = False
            if Game_Over == False:
                if Window.type == pygame.MOUSEBUTTONDOWN and Mouse_Clicked == False:
                    Mouse_Clicked = True
                if Window.type == pygame.MOUSEBUTTONUP and Mouse_Clicked == True:
                    Mouse_Clicked = False
                    Position = pygame.mouse.get_pos()
                    The_X_position = Position[0] // 100
                    The_Y_position = Position[1] // 100
                    if Board[The_X_position][The_Y_position] == 0:
                        Board[The_X_position][The_Y_position] = Player
                        is_the_game_over()
                        print(Board)
                        Player *= -1 
        if Game_Over == True:
            draw_game_over_text(Winner)
            if Window.type == pygame.MOUSEBUTTONDOWN and Mouse_Clicked == False:
                Mouse_Clicked = True
            if Window.type == pygame.MOUSEBUTTONUP and Mouse_Clicked == True:
                Mouse_Clicked = False
                Position = pygame.mouse.get_pos()
                if Play_Again_Box.collidepoint(Position):
                    Game_Over = False
                    Player = 1
                    Position = (0, 0)
                    Board = []
                    Winner = 0
                    emepty_board(Board)

        pygame.display.update()

    pygame.quit()
    sys.exit()


