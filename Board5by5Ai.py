import pygame
from pygame.locals import *
import random
import copy

pygame.init()

Board5X5_Width = 600
Board5X5_Height = 600
Lines_Width = 15
Board_Screen = pygame.display.set_mode((Board5X5_Width, Board5X5_Height)) 
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

Play_Again_Box = Rect(Board5X5_Width // 2 - 130, Board5X5_Height // 2 + 25, 325, 75)


def draw_board():
	BackGround = WHITE
	Grid_Lines = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,5):
		pygame.draw.line(Board_Screen, Grid_Lines , (0, 120 * Grid_Lines), (Board5X5_Width,120 * Grid_Lines), Lines_Width)
		pygame.draw.line(Board_Screen, Grid_Lines, (120 * Grid_Lines, 0), (120 * Grid_Lines, Board5X5_Height), Lines_Width)


# makes X and O
def draw_letter():
	X_Position = 0
	for Spots in Board:
		Y_Position = 0
		for Player in Spots:
			if Player == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 15), (X_Position * 120 + 105, Y_Position * 120 + 105), Lines_Width)
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 120 + 15, Y_Position * 120 + 105), (X_Position * 120 + 105, Y_Position * 120 + 15), Lines_Width)
			if Player == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 120 + 62.5, Y_Position * 120 + 60), 52, Lines_Width)
			Y_Position += 1
		X_Position += 1	


# check the board if game is over
def is_the_game_over():
	# acesss variables outside the function
	global Game_Over
	global Winner

	Letter = 0
	for Spots in Board:
		# checks column for 4 in a row
		if sum(Spots) == 5: # when player 1 place a letter it's + 1
			Winner = 1
			Game_Over = True
		if sum(Spots) == -5: # when player 2 place a letter it's - 1
			Winner = 2
			Game_Over = True
		# checks 4 in a row 
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == 5:
			Winner = 1
			Game_Over = True
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] + Board[4][Letter] == -5:
			Winner = 2
			Game_Over = True
		Letter += 1

	# checks for 4 in a row diagonal 
	if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == 5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == 5:
		Winner = 1
		Game_Over = True
	if Board[0][0] + Board[1][1] + Board[2][2] + Board[3][3] + Board[4][4] == -5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == -5:
		Winner = 2
		Game_Over = True

	# checks for tie game
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

	if winner != 0: # if player 1 or player 2 wins 
		End_Text = "Player " + str(winner) + " wins!"
	elif winner == 0: # if neither player 1 or player 2 wins
		End_Text = "You have tied!"

	# draws end game text and player text below
	End_Img = Font.render(End_Text, True, DARK_BLUE) 
	pygame.draw.rect(Board_Screen, ORANGE, (Board5X5_Width // 2 - 170, Board5X5_Height // 2 - 60, 390, 65))
	Board_Screen.blit(End_Img, (Board5X5_Width // 2 - 150, Board5X5_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board5X5_Width // 2 - 120, Board5X5_Height // 2 + 40))


def computerMove(AiTurn):
	# access variabes outside the function
	global Game_Over 
	global Winner
	Random_Row = random.randint(0, 4) # random move in rows
	Random_Colum = random.randint(0, 4) # random move in column

	"""Makes the Ai be able to move"""
	for Row in range(5): # three rows
		for Colum in range(5): # three columns
			Board_Copy = copy.deepcopy(Board) 
			if Board_Copy[Random_Row][Random_Colum] == 0: # chooses any location on board if it's open
				Board_Copy[Random_Row][Random_Colum] = AiTurn # Ai turn to go
				if is_the_game_over() in Board_Copy: # is the game over in the ai board
					Game_Over = True
					Winner = 2
				else: # if not continue add a letter until game is tied, player 1 wins or the ai wins 
					Ai_Board.append(draw_letter())
					Board_Copy[Random_Row][Random_Colum] = AiTurn
					return Board_Copy

	# Can the Ai place a letter in the box?
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
	validMoves = [] # valid moves
	for Row in range(5): # 3 rows
		for Colum in range(5): # 3 columns
			if Board[Row][Colum] == 0: # any spot with 0
				validMoves.append((Colum, Row)) # adds all aviable moves for the ai to move
	if len(validMoves) > 0: # if any spot is zero you can place a letter
		return random.choice(validMoves)
	else:
		return None	# nothing available 


"""Starts the game"""
def start_4by4_Board():
	# access variabes outside the function
	global Winner
	global Game_Over
	global Position
	global Board
	global Player
	global Mouse_Clicked
	global Ai_Board

	Start_Tic_Tac_Toe = True
	while Start_Tic_Tac_Toe == True:

		# draw board and ready for first click on board
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


		# if someone has won the game
		if Game_Over == True:
			draw_game_over_text(Winner)
			# check for if we clicked on Play Again
			if Window.type == pygame.MOUSEBUTTONDOWN and Mouse_Clicked == False:
				Mouse_Clicked = True
			if Window.type == pygame.MOUSEBUTTONUP and Mouse_Clicked == True:
				Mouse_Clicked = False
				Position = pygame.mouse.get_pos()
				if Play_Again_Box.collidepoint(Position):
					# resets everything
					Game_Over = False
					Player = 1
					Position = (0,0)
					Board = []
					Winner = 0
					Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
					Ai_Board = []

		# updates display
		pygame.display.update()

	pygame.quit()

start_4by4_Board()

