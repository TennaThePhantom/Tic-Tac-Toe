import pygame
from pygame.locals import *
import random
import copy


pygame.init()


Board4X4_Width = 500
Board4X4_Height = 500
line_width = 15

Board_Screen = pygame.display.set_mode((Board4X4_Width, Board4X4_Height)) 
pygame.display.set_caption("Tic Tac Toe 4X4 Board")

# colors for board
ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)


font = pygame.font.SysFont(None,  60)

Mouse_clicked = False
Player = 1
Position = (0,0)
Board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Ai_Board = []
Game_over = False
Winner = 0

Play_Again_Box = Rect(Board4X4_Width // 2 - 110, Board4X4_Height // 2, 265, 50)

def draw_board():
	BackGround = WHITE
	grid = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,4):
		pygame.draw.line(Board_Screen, grid , (0, 125 * Grid_Lines), (Board4X4_Width,125 * Grid_Lines), line_width)
		pygame.draw.line(Board_Screen, grid, (125 * Grid_Lines, 0), (125 * Grid_Lines, Board4X4_Height), line_width)

# makes X and O
def draw_Letter():
	x_position = 0
	for spots in Board:
		y_position = 0
		for player in spots:
			if player == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (x_position * 125 + 15, y_position * 125 + 15), (x_position * 125 + 110, y_position * 125 + 110), line_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 125 + 15, y_position * 125 + 110), (x_position * 125 + 110, y_position * 125 + 15), line_width)
			if player == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 125 + 62.5, y_position * 125 + 62.5), 50, line_width)

			y_position += 1
		x_position += 1	

def Is_the_game_over():
	# acesss variables outside the function
	global Game_over
	global Winner

	Letter = 0
	for spots in Board:
		# checks column for 4 in a row
		if sum(spots) == 4: # when player 1 place a letter it's + 1
			Winner = 1
			Game_over = True
		if sum(spots) == -4: # when player place a letter it's - 1
			Winner = 2
			Game_over = True
		# checks 4 in a row 
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] == 4:
			Winner = 1
			Game_over = True
		if Board[0][Letter] + Board[1][Letter] + Board[2][Letter] + Board[3][Letter] == -4:
			Winner = 2
			Game_over = True
		Letter += 1

	# checks for 4 in a row diagonal 
	if Board[0][0] + Board[1][1] + Board [2][2] + Board[3][3] == 4 or Board[3][0] + Board[2][1] + Board [1][2] + Board[0][3] == 4:
		Winner = 1
		Game_over = True
	if Board[0][0] + Board[1][1] + Board [2][2] + Board[3][3] == -4 or Board[3][0] + Board[2][1] + Board [1][2] + Board[0][3] == -4:
		Winner = 2
		Game_over = True

	# checks for tie game
	if Game_over == False:
		tie = True
		for row in Board:
			for Zero in row:
				if Zero == 0:
					tie = False
		if tie == True:
			Game_over = True
			Winner = 0


def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, (Board4X4_Width // 2 - 150, Board4X4_Height // 2 - 60, 300, 50))
	Board_Screen.blit(end_img, (Board4X4_Width // 2 - 150, Board4X4_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board4X4_Width // 2 - 100, Board4X4_Height // 2 + 10))


def computerMove(AiTurn):
	global Game_over 
	global Winner
	Random_row = random.randint(0, 3) # random move in rows
	Random_colum = random.randint(0, 3) # random move in column


	"""Makes the Ai be able to move"""
	for row in range(4): # three rows
		for colum in range(4): # three columns
			board_copy = copy.deepcopy(Board) 
			if board_copy[Random_row][Random_colum] == 0: # chooses any location on board if it's open
				board_copy[Random_row][Random_colum] = AiTurn # Ai turn to go
				if Is_the_game_over() in board_copy: # is the game over in the ai board
					Game_over = True
					Winner = 2
				else: # if not continue add a letter until game is tied, player 1 wins or the ai wins 
					Ai_Board.append(draw_Letter())
					board_copy[Random_row][Random_colum] = AiTurn
					return board_copy

	"""if the board is full there is no available moves 
	but the Ai needs to know that or else it will try to place a letter and crash the program
	Also the Ai must know the player placed a letter in the box too if not it will try to place a letter 
	in a box with a letter and crash the program"""
	move = Is_the_box_open()
	if move != None: 
		x, y = move
		board_copy = copy.deepcopy(Board)
		board_copy[y][x] = AiTurn
		if AiTurn == -1:
			Ai_Board.append(draw_Letter())
		return board_copy
	return Board


def Is_the_box_open():
	validMoves = [] # valid moves
	for row in range(4): # 3 rows
		for colum in range(4): # 3 columns
			if Board[row][colum] == 0: # any spot with 0
				validMoves.append((colum, row)) # adds all aviable moves for the ai to move
	if len(validMoves) > 0: # if any spot is zero you can place a letter
		return random.choice(validMoves)
	else:
		return None	# nothing available 



"""Starts the game"""
def start_4by4_Board():
	"""access the variables outside the functions"""
	global Winner
	global Game_over
	global Position
	global Board
	global Player
	global Mouse_clicked
	global Ai_Board

	Start_Tic_Tac_Toe = True
	while Start_Tic_Tac_Toe == True:
	
		# draw board and ready for first click on board
		draw_board()
		draw_Letter()
		for window in pygame.event.get():
			if window.type == pygame.QUIT:
				Start_Tic_Tac_Toe = False
			if Game_over == False:
				if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
					Mouse_clicked = True
				if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
					Mouse_clicked = False
					Position = pygame.mouse.get_pos()
					the_X_position = Position[0] // 125
					The_Y_position = Position[1] // 125
					if Board[the_X_position][The_Y_position] == 0:
						Board[the_X_position][The_Y_position] = Player
						if Player == 1:
							Is_the_game_over()
							print(Board)
							if Game_over == True:
								Winner = 1
							else:
								Player *= -1
						if Player == -1:
							Board = computerMove(Player)
							Is_the_game_over()
							print(Board)
							Player *= -1 
		# if someone has won the game
		if Game_over == True:
			draw_game_over(Winner)
			# check for if we clicked on Play Again
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				Position = pygame.mouse.get_pos()
				if Play_Again_Box.collidepoint(Position):
					Game_over = False
					Player = 1
					Position = (0,0)
					Board = []
					Winner = 0
					# creates empty 4 x 4 board again
					Board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
					Ai_Board = []
		# update display
		pygame.display.update()
	
	pygame.quit()

start_4by4_Board()


