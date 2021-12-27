import pygame
from pygame.locals import *


pygame.init()


Board7X7_Height = 700
Board7X7_Width = 700
Lines_Width = 12
Board_Screen = pygame.display.set_mode((Board7X7_Width, Board7X7_Height))
pygame.display.set_caption("Tic-Tac-Toe 7X7 Board")

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

Font = pygame.font.SysFont(None, 90)

Mouse_Clicked = False
Player = 1
Position = (0, 0)
Board = []
Game_Over = False
Winner = 0

for Boxes in range(7):
    Rows = [0] * 7
    Board.append(Rows)


def emepty_board(Board):
    for Boxes in range(7):
        Rows = [0] * 7
        Board.append(Rows)
    print(Board)

Play_Again_Box = Rect(Board7X7_Width // 2 - 200, Board7X7_Height // 2 - 30, 400, 85)

def draw_board():
    Background = WHITE
    Grid = (0, 0, 0)
    Board_Screen.fill(Background)
    for Grid_lines in range(1, 7):
        pygame.draw.line(Board_Screen, Grid, (0, 100 * Grid_lines), (Board7X7_Width, 100 * Grid_lines), Lines_Width)
        pygame.draw.line(Board_Screen, Grid, (100 * Grid_lines, 0), (100 * Grid_lines, Board7X7_Height), Lines_Width)


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
        end_text = "Player " + str(winner) + " wins!"
    elif winner == 0:
        end_text = "You have tied!"

    end_img = Font.render(end_text, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, (Board7X7_Width // 2 - 225, Board7X7_Height // 2 - 150, 470, 80))
    Board_Screen.blit(end_img, (Board7X7_Width // 2 - 195, Board7X7_Height // 2 - 140))

    Play_Again = 'Play Again?'
    Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
    pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
    Board_Screen.blit(Play_Again_IMG, (Board7X7_Width // 2 - 175, Board7X7_Height // 2 - 20))


def how_to_win_colum():
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
    if Board[1][0] + Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][1] + Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][2] + Board[1][3] + Board[1][4] + Board[1][5] + Board[1][6] == 5:
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
    if Board[3][0] + Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][1] + Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[3][2] + Board[3][3] + Board[3][4] + Board[3][5] + Board[3][6] == 5:
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
    if Board[5][0] + Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][1] + Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][2] + Board[5][3] + Board[5][4] + Board[5][5] + Board[5][6] == 5:
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

    if Board[0][0] + Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][2] + Board[0][3] + Board[0][4] + Board[0][5] + Board[0][6] == -5:
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
    if Board[2][0] + Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][1] + Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][2] + Board[2][3] + Board[2][4] + Board[2][5] + Board[2][6] == -5:
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
    if Board[4][0] + Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][1] + Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[4][2] + Board[4][3] + Board[4][4] + Board[4][5] + Board[4][6] == -5:
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
    if Board[6][0] + Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][1] + Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][2] + Board[6][3] + Board[6][4] + Board[6][5] + Board[6][6] == -5:
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
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == 5:
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
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == 5:
        Winner = 1
        Game_Over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == 5:
        Winner = 1
        Game_Over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == 5:
        Winner = 1
        Game_Over = True
    
    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][2] + Board[3][3] + Board[4][4] + Board[5][5] + Board[6][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][1] + Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][2] + Board[2][3] + Board[3][4] + Board[4][5] + Board[5][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[0][2] + Board[1][3] + Board[2][4] + Board[3][5] + Board[4][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[1][0] + Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][1] + Board[3][2] + Board[4][3] + Board[5][4] + Board[6][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[2][0] + Board[3][1] + Board[4][2] + Board[5][3] + Board[6][4] == -5:
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
    if Board[6][1] + Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] == -5:
        Winner = 2
        Game_Over = True
    if Board[6][2] + Board[5][3] + Board[4][4] + Board[3][5] + Board[2][6] == -5:
        Winner = 2
        Game_Over = True
    if Board[5][2] + Board[4][3] + Board[3][4] + Board[2][5] + Board[1][6] == -5:
        Winner = 2
        Game_Over = True


def is_the_game_over():
    global Game_Over
    global Winner

    how_to_win_colum()
    how_to_win_diagonal()

    Letter = 0
    for row in Board: 
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
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == 5:
            Winner = 1
            Game_Over = True
        if Board[2][Letter] + Board[3][Letter] + Board[4][Letter] + Board[5][Letter] + Board[6][Letter] == -5:
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


def Start_7X7_Board():
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
                    The_X_position = Position[0] // 100
                    The_Y_position = Position[1] // 100
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

Start_7X7_Board()


