import pygame
from pygame import rect
from pygame.locals import *




pygame.init()


board7by7_Height = 700
board7b7_Width = 700
lines_width = 15
Board_Screen = pygame.display.set_mode((board7b7_Width, board7by7_Height))
pygame.display.set_caption("Tic Tac Toe 7 by 7 Board")

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 150)

Mouse_clicked = False
player = 1
position = (0,0)
Board = []
game_over = False
winner = 0


for boxes in range(7):
    rows = [0] * 7
    Board.append(rows)


play_again = rect( board7b7_Width // 2 - 300, board7by7_Height // 2 + 30, 600, 70)


def draw_board():
    background = WHITE
    grid = (0, 0, 0)
    Board_Screen.fill(background)
    for Grid_lines in range(1, 5):
        pygame.draw.line(Board_Screen, grid, (0, 100 * Grid_lines), (board7b7_Width, 100 * Grid_lines), lines_width)
        pygame.draw.line(Board_Screen, grid, (100 * Grid_lines, 0), (100 * Grid_lines, board7by7_Height), lines_width)

def draw_letter():
    x_position = 0
    for spots in Board:
        y_position = 0
        for y in spots:
            if y == 1:
                pygame.draw.line(Board_Screen, ROSE, (x_position * 100 + 15, y_position * 100 + 15), (x_position * 100 + 85, y_position * 100 + 85), lines_width)
                pygame.draw.line(Board_Screen, ROSE, (x_position * 100 + 15, y_position * 100 + 15), (x_position * 100 + 85, y_position * 100 + 85), lines_width)
            if y == -1:
                pygame.draw.circle(Board_Screen, ORANGE, (x_position * 100 + 30, y_position * 100 + 30), 52, lines_width)
            y_position += 1
        x_position += 1


def Is_the_game_over():
    global game_over
    global winner

    y_position = 0
    for spots in Board:
        if sum(spots) == 5:
            winner = 1
            game_over = True
        if sum(spots) == -5:
            winner = 2
            game_over = True
        for row in Board:
            if sum(row) == 5:
                winner = 1
                game_over = True
            if sum(row) == -5:
                winner = 2
                game_over = True
    
    if (Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4]) == 5:
        winner = 1
        game_over = True
    if (Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4]) == -5:
        winner = 2
        game_over = True
    
    if game_over == False:
        tie = True
        for row in Board:
            for letter in row:
                if letter == 0:
                    tie = False
        if tie == True:
            game_over = True
            winner = 0
    
def draw_game_over(winner):
    if winner != 0:
        end_text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "You have tied!"

	end_img = font.render(end_text, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, (board7b7_Width // 2 - 230, Board_Height // 2 - 60, 500, 90))

