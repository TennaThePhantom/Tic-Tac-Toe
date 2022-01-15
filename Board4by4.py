import pygame
import sys
from pygame.locals import *

pygame.init()

Board4X4_Width = 500
Board4X4_Height = 500
Lines_Width = 15

Board_Screen = pygame.display.set_mode((Board4X4_Width, Board4X4_Height)) 

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

Font = pygame.font.SysFont(None,  60)

Mouse_Clicked = False
Player = 1
Position = (0,0)
Board = []
Game_Over = False
Winner = 0

for Boxes in range(4):
    Rows = [0] * 4
    Board.append(Rows)

Play_Again_Box = Rect(Board4X4_Width // 2 - 130, Board4X4_Height // 2 + 20, 265, 50)


def draw_board():
	BackGround = WHITE
	Grid_Lines_Color = BLACK
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,4):
		pygame.draw.line(Board_Screen, Grid_Lines_Color , (0, 125 * Grid_Lines), (Board4X4_Width,125 * Grid_Lines), Lines_Width)
		pygame.draw.line(Board_Screen, Grid_Lines_Color, (125 * Grid_Lines, 0), (125 * Grid_Lines, Board4X4_Height), Lines_Width)


def draw_letter():
	X_Position = 0
	for Spots in Board:
		Y_Position = 0
		for Player in Spots:
			if Player == 1: 
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 125 + 15, Y_Position * 125 + 15), (X_Position * 125 + 110, Y_Position * 125 + 110), Lines_Width)
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 125 + 15, Y_Position * 125 + 110), (X_Position * 125 + 110, Y_Position * 125 + 15), Lines_Width)
			if Player == -1: 
				pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 125 + 62.5, Y_Position * 125 + 62.5), 50, Lines_Width)
			Y_Position += 1
		X_Position += 1	


def is_the_game_over():
	global Game_Over
	global Winner

	Letter = 0
	for Spots in Board:
		if sum(Spots) == 4: 
			Winner = 1
			Game_Over = True
		if sum(Spots) == -4: 
			Winner = 2
			Game_Over = True
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] == 4:
			Winner = 1
			Game_Over = True
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] == -4:
			Winner = 2
			Game_Over = True
		Letter += 1

	if Board[0][0] + Board[1][1] + Board [2][2] + Board[3][3] == 4 or Board[3][0] + Board[2][1] + Board[1][2] + Board[0][3] == 4:
		Winner = 1
		Game_Over = True
	if Board[0][0] + Board[1][1] + Board [2][2] + Board[3][3] == -4 or Board[3][0] + Board[2][1] + Board[1][2] + Board[0][3] == -4:
		Winner = 2
		Game_Over = True

	if Game_Over == False:
		Tie = True
		for Row in Board:
			for Zero in Row:
				if Zero == 0:
					Tie = False
		if Tie == True:
			Game_Over = True
			Winner = 0


def draw_game_over_text(winner):

	if winner != 0:
		End_Text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		End_Text = "You have tied!"

	End_Img = Font.render(End_Text, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, (Board4X4_Width // 2 - 150, Board4X4_Height // 2 - 60, 300, 55))
	Board_Screen.blit(End_Img, (Board4X4_Width // 2 - 135, Board4X4_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board4X4_Width // 2 - 120, Board4X4_Height // 2 + 30))

def start_4by4_board():
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
					the_X_position = Position[0] // 125
					The_Y_position = Position[1] // 125
					if Board[the_X_position][The_Y_position] == 0:
						Board[the_X_position][The_Y_position] = Player
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
					Position = (0,0)
					Board = []
					Winner = 0
					Board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

		pygame.display.update()

	pygame.quit()
	sys.exit()


