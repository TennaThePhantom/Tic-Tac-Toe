import sys
import pygame
from pygame.locals import *
import random
import copy

pygame.init()

Ai_Board5X5_Width = 600
Ai_Board5X5_Height = 600
Lines_Width = 15
Board_Screen = pygame.display.set_mode((Ai_Board5X5_Width, Ai_Board5X5_Height)) 
pygame.display.set_caption("Ai Tic-Tac-Toe 5X5 Board")

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

Font = pygame.font.SysFont(None,  75)

Mouse_Clicked = False
Player = 1
Position = (0,0)
Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
Ai_Board = []
Game_Over = False
Winner = 0

Play_Again_Box = Rect(Ai_Board5X5_Width // 2 - 130, Ai_Board5X5_Height // 2 + 25, 325, 75)


def draw_board():
	BackGround = WHITE
	Grid_Lines = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,5):
		pygame.draw.line(Board_Screen, Grid_Lines , (0, 120 * Grid_Lines), (Ai_Board5X5_Width,120 * Grid_Lines), Lines_Width)
		pygame.draw.line(Board_Screen, Grid_Lines, (120 * Grid_Lines, 0), (120 * Grid_Lines, Ai_Board5X5_Height), Lines_Width)


def draw_letter():
	X_Position = 0
	for Spots in Board:
		Y_Position = 0
		for Player in Spots:
			if Player == 1:
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 15), (X_Position * 120 + 105, Y_Position * 120 + 105), Lines_Width)
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 105), (X_Position * 120 + 105, Y_Position * 120 + 15), Lines_Width)
			if Player == -1:
				pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 120 + 62.5, Y_Position * 120 + 60), 52, Lines_Width)
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

		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == 5:
			Winner = 1
			Game_Over = True
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == -5:
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
	pygame.draw.rect(Board_Screen, ORANGE, (Ai_Board5X5_Width // 2 - 170, Ai_Board5X5_Height // 2 - 60, 390, 65))
	Board_Screen.blit(End_Img, (Ai_Board5X5_Width // 2 - 150, Ai_Board5X5_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Ai_Board5X5_Width // 2 - 120, Ai_Board5X5_Height // 2 + 40))


def computerMove(AiTurn):
	global Game_Over 
	global Winner
	Random_Row = random.randint(0, 4)
	Random_Colum = random.randint(0, 4)

	for Row in range(5): 
		for Colum in range(5):
			Board_Copy = copy.deepcopy(Board) 
			if Board_Copy[Random_Row][Random_Colum] == 0: 
				Board_Copy[Random_Row][Random_Colum] = AiTurn 
				if is_the_game_over() in Board_Copy: 
					Game_Over = True
					Winner = 2
				else:
					Ai_Board.append(draw_letter())
					Board_Copy[Random_Row][Random_Colum] = AiTurn
					return Board_Copy

	Move = is_the_box_open()
	if Move != None: 
		x, y = Move
		Board_Copy = copy.deepcopy(Board)
		Board_Copy[y][x] = AiTurn
		if AiTurn == -1:
			Ai_Board.append(draw_letter())
		return Board_Copy
	return Board


def is_the_box_open():
	validMoves = [] 
	for Row in range(5): 
		for Colum in range(5): 
			if Board[Row][Colum] == 0: 
				validMoves.append((Colum, Row)) 
	if len(validMoves) > 0: 
		return random.choice(validMoves)
	else:
		return None

def start_ai_5by5_Board():
	global Winner
	global Game_Over
	global Position
	global Board
	global Player
	global Mouse_Clicked
	global Ai_Board

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
					The_X_Position = Position[0] // 120
					The_Y_Position = Position[1] // 120
					if Board[The_X_Position][The_Y_Position] == 0:
						Board[The_X_Position][The_Y_Position] = Player
						if Player == 1:
							is_the_game_over()
							print(Board)
							if Game_Over == True:
								pass
							else:
								Player *= -1
						if Player == -1:
							Board = computerMove(Player)
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
					Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
					Ai_Board = []

		pygame.display.update()

	pygame.quit()
	sys.exit()

