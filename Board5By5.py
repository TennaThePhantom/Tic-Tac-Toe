import pygame
import sys
from pygame.locals import *

pygame.init()

Board5X5_Height = 600
Board5X5_Width = 600
Lines_Width = 15
Board_Screen = pygame.display.set_mode((Board5X5_Width, Board5X5_Height))
pygame.display.set_caption('Tic-Tac-Toe 5X5 Board')

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

Font = pygame.font.SysFont(None, 75)

Mouse_Clicked = False
Player = 1
Position = (0,0)
Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Game_Over = False
Winner = 0

Play_Again_Box = Rect(Board5X5_Width // 2 - 130, Board5X5_Height // 2 + 25, 325, 75)


def draw_board():
    background = (255, 255, 255)
    Grid_Lines = (0, 0, 0)
    Board_Screen.fill(background)
    for Grid_Lines in range(1, 5): 
        pygame.draw.line(Board_Screen, Grid_Lines, (0, 120 * Grid_Lines), (Board5X5_Width, 120 * Grid_Lines), Lines_Width)
        pygame.draw.line(Board_Screen, Grid_Lines, (120 * Grid_Lines, 0), (120 * Grid_Lines, Board5X5_Height), Lines_Width)


def draw_letter():
    X_Position = 0
    for Spots in Board:
        Y_Position = 0
        for Player in Spots:
            if Player == 1:
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 15), (X_Position * 120 + 105, Y_Position * 120 + 105), Lines_Width)
                pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 105), (X_Position * 120 + 105, Y_Position * 120 + 15), Lines_Width)
            if Player == -1:
                pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 120 + 60, Y_Position * 120 + 60), 52 , Lines_Width)
            Y_Position += 1
        X_Position += 1


def is_the_game_over():
    global Game_Over
    global Winner

    Letter = 0
    for Spots in Board:
        if sum(Spots) == 5: 
            Winner = 1
            Game_Over = True
        if sum(Spots) == -5: 
            Winner = 2
            Game_Over = True

        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] +  Board[3][Letter] + Board[4][Letter] == 5: 
            Winner = 1
            Game_Over = True
        if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] +  Board[3][Letter] + Board[4][Letter] == -5:
            Winner = 2
            Game_Over = True
        Letter += 1
    
    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == 5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == 5:
        Winner = 1
        Game_Over = True
    if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == -5:
        Winner = 2
        Game_Over = True
    
    if Game_Over == False:
        tie = True
        for Row in Board:
            for Zero in Row:
                if Zero == 0:
                    tie = False
        if tie == True:
            Game_Over = True
            Winner = 0


def draw_game_over_text(winner):
	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = Font.render(end_text, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, (Board5X5_Width // 2 - 170, Board5X5_Height // 2 - 60, 390, 65))
	Board_Screen.blit(end_img, (Board5X5_Width // 2 - 150, Board5X5_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board5X5_Width // 2 - 120, Board5X5_Height // 2 + 40))


def start_5by5_Board():
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
                    The_X_position = Position[0] // 120
                    The_Y_position = Position[1] // 120
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
                    Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        pygame.display.update()

    pygame.quit()
    sys.exit()


