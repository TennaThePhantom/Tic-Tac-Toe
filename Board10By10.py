import pygame
from pygame.locals import *


pygame.init()


board10by10_Height = 800
board10by10_Width = 800
lines_width = 12
Board_Screen = pygame.display.set_mode((board10by10_Width, board10by10_Height))
pygame.display.set_caption("Tic Tac Toe 7 by 7 Board")

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 120)

Mouse_clicked = False
player = 1
position = (0, 0)
Board = []
game_over = False
winner = 0

for boxes in range(10):
    rows = [0] * 10
    Board.append(rows)

""" Creates the [0, 0, 0, 0, 0, 0, 0] Instead of having me to hardcode it
have to be print(Board) first
doesn't work if you called emepty_board instead"""

def Emepty_Board(Board):
    for boxes in range(10):
        rows = [0] * 10
        Board.append(rows)
    print(Board)


Play_Again_Box = Rect(board10by10_Width // 2 - 300, board10by10_Height // 2 - 50, 600, 85)


def draw_board():
    background = WHITE
    grid = (0, 0, 0)
    Board_Screen.fill(background)
    for Grid_lines in range(1, 10):
        pygame.draw.line(Board_Screen, grid, (0, 80 * Grid_lines), (board10by10_Width, 80 * Grid_lines), lines_width)
        pygame.draw.line(Board_Screen, grid, (80 * Grid_lines, 0), (80 * Grid_lines, board10by10_Height), lines_width)


def draw_letter():
    x_position = 0
    for spots in Board:
        y_position = 0
        for player in spots:
            if player == 1:
                pygame.draw.line(Board_Screen, ROSE, (x_position * 80 + 15, y_position * 80 + 15), (x_position * 80 + 65, y_position * 80 + 65), lines_width)
                pygame.draw.line(Board_Screen, ROSE, (x_position * 80 + 15, y_position * 80 + 65), (x_position * 80 + 65, y_position * 80 + 15), lines_width)
            if player == -1:
                pygame.draw.circle(Board_Screen, ORANGE, (x_position * 80 + 40, y_position * 80 + 40), 32, lines_width)
            y_position += 1
        x_position += 1


def draw_game_over(winner):
    if winner != 0:
        end_text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "You have tied!"

    end_img = font.render(end_text, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, (board10by10_Width // 2 - 300, board10by10_Height // 2 - 150, 600, 90))
    Board_Screen.blit(end_img, (board10by10_Width // 2 - 300, board10by10_Height // 2 - 150))

    Play_Again = 'Play Again?'
    Play_Again_IMG = font.render(Play_Again, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
    Board_Screen.blit(Play_Again_IMG, (board10by10_Width // 2 - 250, board10by10_Height // 2 - 50))


def Player_1_colum_win():
    global game_over
    global winner

    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == 5:
        winner = 1
        game_over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == 5:
        winner = 1
        game_over = True
    if Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] == 5:
        winner = 1
        game_over = True
    if Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] == 5:
        winner = 1
        game_over = True
    if Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] == 5:
        winner = 1
        game_over = True
    if Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] + Board[0][9] == 5:
        winner = 1
        game_over = True

    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == 5:
        winner = 1
        game_over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == 5:
        winner = 1
        game_over = True
    if Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] == 5:
        winner = 1
        game_over = True
    if Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] == 5:
        winner = 1
        game_over = True
    if Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] == 5:
        winner = 1
        game_over = True
    if Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] + Board[1][9] == 5:
        winner = 1
        game_over = True

    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == 5:
        winner = 1
        game_over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == 5:
        winner = 1
        game_over = True
    if Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] == 5:
        winner = 1
        game_over = True
    if Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] == 5:
        winner = 1
        game_over = True
    if Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] == 5:
        winner = 1
        game_over = True
    if Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] + Board[2][9] == 5:
        winner = 1
        game_over = True
    
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == 5:
        winner = 1
        game_over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == 5:
        winner = 1
        game_over = True
    if Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] == 5:
        winner = 1
        game_over = True
    if Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] == 5:
        winner = 1
        game_over = True
    if Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] == 5:
        winner = 1
        game_over = True
    if Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] + Board[3][9] == 5:
        winner = 1
        game_over = True

    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == 5:
        winner = 1
        game_over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == 5:
        winner = 1
        game_over = True
    if Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] == 5:
        winner = 1
        game_over = True
    if Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] == 5:
        winner = 1
        game_over = True
    if Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] == 5:
        winner = 1
        game_over = True
    if Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] + Board[4][9] == 5:
        winner = 1
        game_over = True


    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == 5:
        winner = 1
        game_over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == 5:
        winner = 1
        game_over = True
    if Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] == 5:
        winner = 1
        game_over = True
    if Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] == 5:
        winner = 1
        game_over = True
    if Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] == 5:
        winner = 1
        game_over = True
    if Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] + Board[5][9] == 5:
        winner = 1
        game_over = True

    if Board[6][0] + Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] == 5:
        winner = 1
        game_over = True
    if Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] == 5:
        winner = 1
        game_over = True
    if Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] == 5:
        winner = 1
        game_over = True
    if Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] == 5:
        winner = 1
        game_over = True
    if Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] == 5:
        winner = 1
        game_over = True
    if Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] + Board[6][9] == 5:
        winner = 1
        game_over = True
    
    if Board[7][0] + Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] == 5:
        winner = 1
        game_over = True
    if Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] == 5:
        winner = 1
        game_over = True
    if Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] == 5:
        winner = 1
        game_over = True
    if Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] == 5:
        winner = 1
        game_over = True
    if Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] == 5:
        winner = 1
        game_over = True
    if Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] + Board[7][9] == 5:
        winner = 1
        game_over = True

    if Board[8][0] + Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] == 5:
        winner = 1
        game_over = True
    if Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] == 5:
        winner = 1
        game_over = True
    if Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] == 5:
        winner = 1
        game_over = True
    if Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] == 5:
        winner = 1
        game_over = True
    if Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] == 5:
        winner = 1
        game_over = True
    if Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] + Board[8][9] == 5:
        winner = 1
        game_over = True

    if Board[9][0] + Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] == 5:
        winner = 1
        game_over = True
    if Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] == 5:
        winner = 1
        game_over = True
    if Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] == 5:
        winner = 1
        game_over = True
    if Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] == 5:
        winner = 1
        game_over = True
    if Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] == 5:
        winner = 1
        game_over = True
    if Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] + Board[9][9] == 5:
        winner = 1
        game_over = True



def Player_2_colum_win():
    global winner
    global game_over


    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == -5:
        winner = 2
        game_over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == -5:
        winner = 2
        game_over = True
    if Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] == -5:
        winner = 2
        game_over = True
    if Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] == -5:
        winner = 2
        game_over = True
    if Board[0][4] + Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] == -5:
        winner = 2
        game_over = True
    if Board[0][5] + Board[0][6] + Board[0][7] + Board[0][8] + Board[0][9] == -5:
        winner = 2
        game_over = True

    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == -5:
        winner = 2
        game_over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == -5:
        winner = 2
        game_over = True
    if Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] == -5:
        winner = 2
        game_over = True
    if Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] == -5:
        winner = 2
        game_over = True
    if Board[1][4] + Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] == -5:
        winner = 2
        game_over = True
    if Board[1][5] + Board[1][6] + Board[1][7] + Board[1][8] + Board[1][9] == -5:
        winner = 2
        game_over = True

    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == -5:
        winner = 2
        game_over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == -5:
        winner = 2
        game_over = True
    if Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] == -5:
        winner = 2
        game_over = True
    if Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] == -5:
        winner = 2
        game_over = True
    if Board[2][4] + Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] == -5:
        winner = 2
        game_over = True
    if Board[2][5] + Board[2][6] + Board[2][7] + Board[2][8] + Board[2][9] == -5:
        winner = 2
        game_over = True
    
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == -5:
        winner = 2
        game_over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == -5:
        winner = 2
        game_over = True
    if Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] == -5:
        winner = 2
        game_over = True
    if Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] == -5:
        winner = 2
        game_over = True
    if Board[3][4] + Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] == -5:
        winner = 2
        game_over = True
    if Board[3][5] + Board[3][6] + Board[3][7] + Board[3][8] + Board[3][9] == -5:
        winner = 2
        game_over = True

    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == -5:
        winner = 2
        game_over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == -5:
        winner = 2
        game_over = True
    if Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] == -5:
        winner = 2
        game_over = True
    if Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] == -5:
        winner = 2
        game_over = True
    if Board[4][4] + Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] == -5:
        winner = 2
        game_over = True
    if Board[4][5] + Board[4][6] + Board[4][7] + Board[4][8] + Board[4][9] == -5:
        winner = 2
        game_over = True


    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == -5:
        winner = 2
        game_over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == -5:
        winner = 2
        game_over = True
    if Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] == -5:
        winner = 2
        game_over = True
    if Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] == -5:
        winner = 2
        game_over = True
    if Board[5][4] + Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] == -5:
        winner = 2
        game_over = True
    if Board[5][5] + Board[5][6] + Board[5][7] + Board[5][8] + Board[5][9] == -5:
        winner = 2
        game_over = True

    if Board[6][0] + Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] == -5:
        winner = 2
        game_over = True
    if Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] == -5:
        winner = 2
        game_over = True
    if Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] == -5:
        winner = 2
        game_over = True
    if Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] == -5:
        winner = 2
        game_over = True
    if Board[6][4] + Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] == -5:
        winner = 2
        game_over = True
    if Board[6][5] + Board[6][6] + Board[6][7] + Board[6][8] + Board[6][9] == -5:
        winner = 2
        game_over = True
    
    if Board[7][0] + Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] == -5:
        winner = 2
        game_over = True
    if Board[7][1] + Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] == -5:
        winner = 2
        game_over = True
    if Board[7][2] + Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] == -5:
        winner = 2
        game_over = True
    if Board[7][3] + Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] == -5:
        winner = 2
        game_over = True
    if Board[7][4] + Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] == -5:
        winner = 2
        game_over = True
    if Board[7][5] + Board[7][6] + Board[7][7] + Board[7][8] + Board[7][9] == -5:
        winner = 2
        game_over = True

    if Board[8][0] + Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] == -5:
        winner = 2
        game_over = True
    if Board[8][1] + Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] == -5:
        winner = 2
        game_over = True
    if Board[8][2] + Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] == -5:
        winner = 2
        game_over = True
    if Board[8][3] + Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] == -5:
        winner = 2
        game_over = True
    if Board[8][4] + Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] == -5:
        winner = 2
        game_over = True
    if Board[8][5] + Board[8][6] + Board[8][7] + Board[8][8] + Board[8][9] == -5:
        winner = 2
        game_over = True

    if Board[9][0] + Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] == -5:
        winner = 2
        game_over = True
    if Board[9][1] + Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] == -5:
        winner = 2
        game_over = True
    if Board[9][2] + Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] == -5:
        winner = 2
        game_over = True
    if Board[9][3] + Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] == -5:
        winner = 2
        game_over = True
    if Board[9][4] + Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] == -5:
        winner = 2
        game_over = True
    if Board[9][5] + Board[9][6] + Board[9][7] + Board[9][8] + Board[9][9] == -5:
        winner = 2
        game_over = True



def player_1_diagonal_win():
    global winner
    global game_over

    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == 5:
        winner = 1
        game_over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == 5:
        winner = 1
        game_over = True
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == 5:
        winner = 1
        game_over = True
    if Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] == 5:
        winner = 1
        game_over = True
    if Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] == 5:
        winner = 1
        game_over = True
    if Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] + Board[9][9] == 5:
        winner = 1
        game_over = True


    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == 5:
        winner = 1
        game_over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == 5:
        winner = 1
        game_over = True
    if Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] == 5:
        winner = 1
        game_over = True
    if Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] == 5:
        winner = 1
        game_over = True
    if Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] + Board[8][9] == 5:
        winner = 1
        game_over = True

    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == 5:
        winner = 1
        game_over = True
    if Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] == 5:
        winner = 1
        game_over = True
    if Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] == 5:
        winner = 1
        game_over = True
    if Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] + Board[7][9] == 5:
        winner = 1
        game_over = True

    if Board[0][3] + Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] == 5:
        winner = 1
        game_over = True
    if Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] == 5:
        winner = 1
        game_over = True
    if Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] + Board[6][9] == 5:
        winner = 1
        game_over = True

    if Board[0][4] + Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] == 5:
        winner = 1
        game_over = True
    if Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] + Board[5][9]== 5:
        winner = 1
        game_over = True
    if Board[0][5] + Board[1][6] + Board[2][7] + Board[3][8] + Board[4][9] == 5:
        winner = 1
        game_over = True
    
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == 5:
        winner = 1
        game_over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == 5:
        winner = 1
        game_over = True
    if Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] == 5:
        winner = 1
        game_over = True
    if Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] == 5:
        winner = 1
        game_over = True
    if Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] + Board[9][8] == 5:
        winner = 1
        game_over = True

    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == 5:
        winner = 1
        game_over = True
    if Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] == 5:
        winner = 1
        game_over = True
    if Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] == 5:
        winner = 1
        game_over = True
    if Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] + Board[9][7] == 5:
        winner = 1
        game_over = True
    
    if Board[3][0] + Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] == 5:
        winner = 1
        game_over = True
    if Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] == 5:
        winner = 1
        game_over = True
    if Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] + Board[9][6] == 5:
        winner = 1
        game_over = True

    
    if Board[4][0] + Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] == 5:
        winner = 1
        game_over = True
    if Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] + Board[9][5] == 5:
        winner = 1
        game_over = True

    if Board[5][0] + Board[6][1] + Board[7][2] + Board[8][3] + Board[9][4] == 5:
        winner = 1
        game_over = True
    
    if Board[9][0] + Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] == 5:
        winner = 1
        game_over = True
    if Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] == 5:
        winner = 1
        game_over = True
    if Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] == 5:
        winner = 1
        game_over = True
    if Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] == 5:
        winner = 1
        game_over = True
    if Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] == 5:
        winner = 1
        game_over = True
    if Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] + Board[0][9] == 5:
        winner = 1
        game_over = True


    if Board[9][1] + Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] == 5:
        winner = 1
        game_over = True
    if Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] == 5:
        winner = 1
        game_over = True
    if Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] == 5:
        winner = 1
        game_over = True
    if Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] == 5:
        winner = 1
        game_over = True
    if Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] + Board[1][9] == 5:
        winner = 1
        game_over = True

    if Board[9][2] + Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] == 5:
        winner = 1
        game_over = True
    if Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] == 5:
        winner = 1
        game_over = True
    if Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] == 5:
        winner = 1
        game_over = True
    if Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] + Board[2][9] == 5:
        winner = 1
        game_over = True

    
    if Board[9][3] + Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] == 5:
        winner = 1
        game_over = True
    if Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] == 5:
        winner = 1
        game_over = True
    if Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] + Board[3][9] == 5:
        winner = 1
        game_over = True

    if Board[9][4] + Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] == 5:
        winner = 1
        game_over = True
    if Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] + Board[4][9] == 5:
        winner = 1
        game_over = True
    
    if Board[9][5] + Board[8][6] + Board[7][7] + Board[6][8] + Board[5][9] == 5:
        winner = 1
        game_over = True
    
    if Board[8][0] + Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] == 5:
        winner = 1
        game_over = True
    if Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] == 5:
        winner = 1
        game_over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == 5:
        winner = 1
        game_over = True
    if Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] == 5:
        winner = 1
        game_over = True
    if Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] + Board[0][8] == 5:
        winner = 1
        game_over = True
    
    if Board[7][0] + Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] == 5:
        winner = 1
        game_over = True
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == 5:
        winner = 1
        game_over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == 5:
        winner = 1
        game_over = True
    if Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] + Board[0][7] == 5:
        winner = 1
        game_over = True


    if Board[6][0] + Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] == 5:
        winner = 1
        game_over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == 5:
        winner = 1
        game_over = True
    if Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] + Board[0][6] == 5:
        winner = 1
        game_over = True
    
    if Board[5][0] + Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] == 5:
        winner = 1
        game_over = True
    if Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] + Board[0][5] == 5:
        winner = 1
        game_over = True
    
    if Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == 5:
        winner = 1
        game_over = True



def player_2_diagonal_win():

    global winner
    global game_over

    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5:
        winner = 2
        game_over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == -5:
        winner = 2
        game_over = True
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == -5:
        winner = 2
        game_over = True
    if Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] == -5:
        winner = 2
        game_over = True
    if Board[4][4] + Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] == -5:
        winner = 2
        game_over = True
    if Board[5][5] + Board[6][6] + Board[7][7] + Board[8][8] + Board[9][9] == -5:
        winner = 2
        game_over = True


    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == -5:
        winner = 2
        game_over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == -5:
        winner = 2
        game_over = True
    if Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] == -5:
        winner = 2
        game_over = True
    if Board[3][4] + Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] == -5:
        winner = 2
        game_over = True
    if Board[4][5] + Board[5][6] + Board[6][7] + Board[7][8] + Board[8][9] == -5:
        winner = 2
        game_over = True

    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == -5:
        winner = 2
        game_over = True
    if Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] == -5:
        winner = 2
        game_over = True
    if Board[2][4] + Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] == -5:
        winner = 2
        game_over = True
    if Board[3][5] + Board[4][6] + Board[5][7] + Board[6][8] + Board[7][9] == -5:
        winner = 2
        game_over = True

    if Board[0][3] + Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] == -5:
        winner = 2
        game_over = True
    if Board[1][4] + Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] == -5:
        winner = 2
        game_over = True
    if Board[2][5] + Board[3][6] + Board[4][7] + Board[5][8] + Board[6][9] == -5:
        winner = 2
        game_over = True

    if Board[0][4] + Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] == -5:
        winner = 2
        game_over = True
    if Board[1][5] + Board[2][6] + Board[3][7] + Board[4][8] + Board[5][9]== -5:
        winner = 2
        game_over = True
    if Board[0][5] + Board[1][6] + Board[2][7] + Board[3][8] + Board[4][9] == -5:
        winner = 2
        game_over = True
    
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == -5:
        winner = 2
        game_over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == -5:
        winner = 2
        game_over = True
    if Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] == -5:
        winner = 2
        game_over = True
    if Board[4][3] + Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] == -5:
        winner = 2
        game_over = True
    if Board[5][4] + Board[6][5] + Board[7][6] + Board[8][7] + Board[9][8] == -5:
        winner = 2
        game_over = True

    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == -5:
        winner = 2
        game_over = True
    if Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] == -5:
        winner = 2
        game_over = True
    if Board[4][2] + Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] == -5:
        winner = 2
        game_over = True
    if Board[5][3] + Board[6][4] + Board[7][5] + Board[8][6] + Board[9][7] == -5:
        winner = 2
        game_over = True
    
    if Board[3][0] + Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] == -5:
        winner = 2
        game_over = True
    if Board[4][1] + Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] == -5:
        winner = 2
        game_over = True
    if Board[5][2] + Board[6][3] + Board[7][4] + Board[8][5] + Board[9][6] == -5:
        winner = 2
        game_over = True

    
    if Board[4][0] + Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] == -5:
        winner = 2
        game_over = True
    if Board[5][1] + Board[6][2] + Board[7][3] + Board[8][4] + Board[9][5] == -5:
        winner = 2
        game_over = True

    if Board[5][0] + Board[6][1] + Board[7][2] + Board[8][3] + Board[9][4] == -5:
        winner = 2
        game_over = True
    
    if Board[9][0] + Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] == -5:
        winner = 2
        game_over = True
    if Board[8][1] + Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] == -5:
        winner = 2
        game_over = True
    if Board[7][2] + Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] == -5:
        winner = 2
        game_over = True
    if Board[6][3] + Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] == -5:
        winner = 2
        game_over = True
    if Board[5][4] + Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] == -5:
        winner = 2
        game_over = True
    if Board[4][5] + Board[3][6] + Board[2][7] + Board[1][8] + Board[0][9] == -5:
        winner = 2
        game_over = True


    if Board[9][1] + Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] == -5:
        winner = 2
        game_over = True
    if Board[8][2] + Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] == -5:
        winner = 2
        game_over = True
    if Board[7][3] + Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] == -5:
        winner = 2
        game_over = True
    if Board[6][4] + Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] == -5:
        winner = 2
        game_over = True
    if Board[5][5] + Board[4][6] + Board[3][7] + Board[2][8] + Board[1][9] == -5:
        winner = 2
        game_over = True

    if Board[9][2] + Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] == -5:
        winner = 2
        game_over = True
    if Board[8][3] + Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] == -5:
        winner = 2
        game_over = True
    if Board[7][4] + Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] == -5:
        winner = 2
        game_over = True
    if Board[6][5] + Board[5][6] + Board[4][7] + Board[3][8] + Board[2][9] == -5:
        winner = 2
        game_over = True

    
    if Board[9][3] + Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] == -5:
        winner = 2
        game_over = True
    if Board[8][4] + Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] == -5:
        winner = 2
        game_over = True
    if Board[7][5] + Board[6][6] + Board[5][7] + Board[4][8] + Board[3][9] == -5:
        winner = 2
        game_over = True

    if Board[9][4] + Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] == -5:
        winner = 2
        game_over = True
    if Board[8][5] + Board[7][6] + Board[6][7] + Board[5][8] + Board[4][9] == -5:
        winner = 2
        game_over = True
    
    if Board[9][5] + Board[8][6] + Board[7][7] + Board[6][8] + Board[5][9] == -5:
        winner = 2
        game_over = True
    
    if Board[8][0] + Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] == -5:
        winner = 2
        game_over = True
    if Board[7][1] + Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] == -5:
        winner = 2
        game_over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == -5:
        winner = 2
        game_over = True
    if Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] == -5:
        winner = 2
        game_over = True
    if Board[4][4] + Board[3][5] + Board[2][6] + Board[1][7] + Board[0][8] == -5:
        winner = 2
        game_over = True
    
    if Board[7][0] + Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] == -5:
        winner = 2
        game_over = True
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == -5:
        winner = 2
        game_over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == -5:
        winner = 2
        game_over = True
    if Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] + Board[0][7] == -5:
        winner = 2
        game_over = True


    if Board[6][0] + Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] == -5:
        winner = 2
        game_over = True
    if Board[5][1] + Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] == -5:
        winner = 2
        game_over = True
    if Board[4][2] + Board[3][3] + Board[2][4] + Board[1][5] + Board[0][6] == -5:
        winner = 2
        game_over = True
    
    if Board[5][0] + Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] == -5:
        winner = 2
        game_over = True
    if Board[4][1] + Board[3][2] + Board[2][3] + Board[1][4] + Board[0][5] == -5:
        winner = 2
        game_over = True
    
    if Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == -5:
        winner = 2
        game_over = True




def Did_you_win():

    global game_over
    global winner
    Letter = 0
    """How to wim in colum"""
    Player_1_colum_win()
    Player_2_colum_win()

    """How to win diagonal"""
    player_1_diagonal_win()
    player_2_diagonal_win()

    for row in Board:
        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == 5:
            winner = 1
            game_over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == 5:
            winner = 1
            game_over = True
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == 5:
            winner = 1
            game_over = True
        if Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] == 5:
            winner = 1
            game_over = True
        if Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] == 5:
            winner = 1
            game_over = True
        if Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] + Board[9][Letter] == 5:
            winner = 1
            game_over = True

        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == -5:
            winner = 2
            game_over = True
        if Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] == -5:
            winner = 2
            game_over = True
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == -5:
            winner = 2
            game_over = True
        if Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] == -5:
            winner = 2
            game_over = True
        if Board[4][Letter] + Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] == -5:
            winner = 2
            game_over = True
        if Board[5][Letter] + Board[6][Letter] + Board[7][Letter] + Board[8][Letter] + Board[9][Letter] == -5:
            winner = 2
            game_over = True
        Letter += 1

    """Tie Game"""
    if game_over == False:
        tie = True
        for every_row in Board:
            for Zero in every_row:
                if Zero == 0:
                    tie = False
        if tie == True:
            game_over = True
            winner = 0


def Start_10_by_10_Board():
    global winner
    global game_over
    global position
    global Board
    global player
    global Mouse_clicked
    Start_Tic_Tac_Toe = True
    while Start_Tic_Tac_Toe == True:
        draw_board() 
        draw_letter()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                Start_Tic_Tac_Toe = False
            if game_over == False:
                if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
                    Mouse_clicked = True
                if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
                    Mouse_clicked = False
                    position = pygame.mouse.get_pos()
                    The_X_position = position[0] // 80
                    The_Y_position = position[1] // 80
                    if Board[The_X_position][The_Y_position] == 0:
                        Board[The_X_position][The_Y_position] = player
                        player *= -1
                        print(Board)
                        Did_you_win()

        if game_over == True:
            draw_game_over(winner)
            if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
                Mouse_clicked = True
            if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
                Mouse_clicked = False
                position = pygame.mouse.get_pos()
                if Play_Again_Box.collidepoint(position):
                    game_over = False
                    player = 1
                    position = (0, 0)
                    Board = []
                    winner = 0
                    Emepty_Board(Board)
                    
        pygame.display.update()


Start_10_by_10_Board()



