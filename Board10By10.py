import pygame
import sys
from pygame.locals import *


pygame.init()

Board10X10_Height = 800
Board10X10_Width = 800
Lines_Width = 10
Board_Screen = pygame.display.set_mode((Board10X10_Width, Board10X10_Height))
pygame.display.set_caption("Tic-Tac-Toe 10X10 Board")

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

Font = pygame.font.SysFont(None, 100)

Mouse_Clicked = False
Player = 1
Position = (0, 0)
Board = []
Game_Over = False
Winner = 0

for Boxes in range(10):
    Rows = [0] * 10
    Board.append(Rows)

def emepty_board(Board):
    for Boxes in range(10):
        Rows = [0] * 10
        Board.append(Rows)
    print(Board)

Play_Again_Box = Rect(Board10X10_Width // 2 - 250, Board10X10_Height // 2 + 10, 480, 85)


def draw_board():
    Background = WHITE
    Grid = BLACK
    Board_Screen.fill(Background)
    for Grid_lines in range(1, 10):
        pygame.draw.line(Board_Screen, Grid, (0, 80 * Grid_lines), (Board10X10_Width, 80 * Grid_lines), Lines_Width)
        pygame.draw.line(Board_Screen, Grid, (80 * Grid_lines, 0), (80 * Grid_lines, Board10X10_Height), Lines_Width)


def draw_letter():
    X_Position = 0
    for Spots in Board:
        Y_Position = 0
        for Player in Spots:
            if Player == 1:
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 80 + 15, Y_Position * 80 + 15), (X_Position * 80 + 65, Y_Position * 80 + 65), Lines_Width)
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 80 + 15, Y_Position * 80 + 65), (X_Position * 80 + 65, Y_Position * 80 + 15), Lines_Width)
            if Player == -1:
                pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 80 + 40, Y_Position * 80 + 40), 32, Lines_Width)
            Y_Position += 1
        X_Position += 1


def draw_game_over_text(winner):
    if winner != 0:
        End_Text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        End_Text = "You have tied!"

    End_Img = Font.render(End_Text, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, (Board10X10_Width // 2 - 300, Board10X10_Height // 2 - 110, 570, 90))
    Board_Screen.blit(End_Img, (Board10X10_Width // 2 - 250, Board10X10_Height // 2 - 100))

    Play_Again = 'Play Again?'
    Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
    Board_Screen.blit(Play_Again_IMG, (Board10X10_Width // 2 - 200, Board10X10_Height // 2 + 20))


def player_1_colum_win():
    global Game_Over
    global Winner

    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] + Board[0][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] + Board[1][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] + Board[2][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] + Board[3][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] + Board[4][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] + Board[5][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][0] + Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] + Board[6][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][0] + Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] + Board[7][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][0] + Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] + Board[8][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][0] + Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] + Board[9][9] == 5:
        Winner = 1
        Game_Over = True


def player_2_colum_win():
    global Winner
    global Game_Over

    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] + Board[0][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] + Board[1][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] + Board[2][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] + Board[3][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] + Board[4][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] + Board[5][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][0] + Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] + Board[6][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][0] + Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] + Board[7][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][0] + Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] + Board[8][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][0] + Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] + Board[9][9] == -5:
        Winner = 2
        Game_Over = True


def player_1_diagonal_win():
    global Winner
    global Game_Over

    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] + Board[9][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] + Board[8][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] + Board[7][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][3] + Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] + Board[6][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][4] + Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] + Board[5][9]== 5:
        Winner = 1
        Game_Over = True
    if Board[0][5] + Board[1][6] + Board[2][7] + Board[3][8] + Board[4][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] + Board[9][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] + Board[9][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][0] + Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] + Board[9][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][0] + Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] + Board[9][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][0] + Board[6][1] + Board[7][2] + Board[8][3] + Board[9][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][0] + Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] + Board[0][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][1] + Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] + Board[1][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][2] + Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] + Board[2][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][3] + Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] + Board[3][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][4] + Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] + Board[4][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[9][5] + Board[8][6] + Board[7][7] + Board[6][8] + Board[5][9] == 5:
        Winner = 1
        Game_Over = True
    if Board[8][0] + Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] + Board[0][8] == 5:
        Winner = 1
        Game_Over = True
    if Board[7][0] + Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] + Board[0][7] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][0] + Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] + Board[0][6] == 5:
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


def player_2_diagonal_win():
    global Winner
    global Game_Over

    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] + Board[9][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] + Board[8][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] + Board[7][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][3] + Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] + Board[6][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][4] + Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] + Board[5][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][5] + Board[1][6] + Board[2][7] + Board[3][8] + Board[4][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] + Board[9][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] + Board[9][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[3][0] + Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] + Board[9][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][0] + Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] + Board[9][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][0] + Board[6][1] + Board[7][2] + Board[8][3] + Board[9][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][0] + Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] + Board[0][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][1] + Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] + Board[1][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][2] + Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] + Board[2][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][3] + Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] + Board[3][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][4] + Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] + Board[4][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[9][5] + Board[8][6] + Board[7][7] + Board[6][8] + Board[5][9] == -5:
        Winner = 2
        Game_Over = True
    if Board[8][0] + Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] + Board[0][8] == -5:
        Winner = 2
        Game_Over = True
    if Board[7][0] + Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] + Board[0][7] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][0] + Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] + Board[0][6] == -5:
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
    Letter = 0
    """How to wim in colum"""
    player_1_colum_win()
    player_2_colum_win()

    """How to win diagonal"""
    player_1_diagonal_win()
    player_2_diagonal_win()

    for row in Board:
        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] + Board[9][Letter] == 5:
            Winner = 1
            Game_Over = True

        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] == -5:
            Winner = 2
            Game_Over = True
        if Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] + Board[9][Letter] == -5:
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


def start_10X10_Board():
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
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                Start_Tic_Tac_Toe = False
            if Game_Over == False:
                if window.type == pygame.MOUSEBUTTONDOWN and Mouse_Clicked == False:
                    Mouse_Clicked = True
                if window.type == pygame.MOUSEBUTTONUP and Mouse_Clicked == True:
                    Mouse_Clicked = False
                    Position = pygame.mouse.get_pos()
                    The_X_position = Position[0] // 80
                    The_Y_position = Position[1] // 80
                    if Board[The_X_position][The_Y_position] == 0:
                        Board[The_X_position][The_Y_position] = Player
                        is_the_game_over()
                        print(Board)
                        Player *= -1
        if Game_Over == True:
            draw_game_over_text(Winner)
            if window.type == pygame.MOUSEBUTTONDOWN and Mouse_Clicked == False:
                Mouse_Clicked = True
            if window.type == pygame.MOUSEBUTTONUP and Mouse_Clicked == True:
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


