#import modules
import pygame
import random
import copy
from pygame.locals import *

pygame.init()

# the board
Board_Height = 450
Board_Width = 450
line_width = 15

Board_Screen = pygame.display.set_mode((Board_Width, Board_Height))
pygame.display.set_caption('Ai Tic Tac Toe 3X3 Board')

# colors for board
ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)


# define font
font = pygame.font.SysFont(None, 40)

# variables for game
Mouse_clicked = False
player = 1
position = (0,0)
Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Ai_Board = []
game_over = False
winner = 0

# draws a rectangle around play again 
Play_Again_Box = Rect(Board_Width // 2 - 80, Board_Height // 2, 160, 50)



# makes the board
def draw_board():
	BackGround = WHITE
	grid = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,3):
		"""I got 150 from doing 450 / 3 since I'm having 3 rows and column"""
		pygame.draw.line(Board_Screen, grid , (0, 150 * Grid_Lines), (Board_Width,150 * Grid_Lines), line_width)
		pygame.draw.line(Board_Screen, grid, (150 * Grid_Lines, 0), (150 * Grid_Lines, Board_Height), line_width)

# makes X and O
def draw_Letter():
	x_position = 0
	for spots in Board:
		y_position = 0
		for player in spots:
			if player == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 25), (x_position * 150 + 125, y_position * 150 + 125), line_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 125), (x_position * 150 + 125, y_position * 150 + 25), line_width)
				"""The first number 25 is where the line starts and
					the second number 125 is when the lines ends
					both combine have to equal whatever your board is divide 
					by the amount of rows you have"""
			if player == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 150 + 75, y_position * 150 + 75), 50, line_width)
			"""what's half of 150. 75 to place the circle in the middle of the box
			and the other number is the size of the circle
			you have to play around with that to get the circle size you want"""
			y_position += 1
		x_position += 1	

"""Checks the board if player 1 or 2 have won or is it a tie game(is the board full)"""
def Is_the_game_over():
	# acesss variables outside the function
	global game_over
	global winner

	Letter = 0
	for spots in Board:
		# checks column for 3 in a row
		if sum(spots) == 3: # when player 1 place a letter it's + 1
			winner = 1
			game_over = True
		if sum(spots) == -3: # when player place a letter it's - 1
			winner = 2
			game_over = True
		# checks for 3 in a row 
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == 3:
			winner = 1
			game_over = True
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == -3:
			winner = 2
			game_over = True
		Letter += 1

	# checks for 3 in a row diagonal 
	if Board[0][0] + Board[1][1] + Board [2][2] == 3 or Board[2][0] + Board[1][1] + Board [0][2] == 3:
		winner = 1
		game_over = True
	if Board[0][0] + Board[1][1] + Board [2][2] == -3 or Board[2][0] + Board[1][1] + Board [0][2] == -3:
		winner = 2
		game_over = True

	# checks for tie game
	if game_over == False:
		tie = True
		for row in Board:
			for Zero in row:
				if Zero == 0:
					tie = False
		if tie == True:
			game_over = True
			winner = 0


"""Makes the text when game is over or tie game"""
def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, DARK_BLUE)
	"""Either play around with draw.rect and blit for this part or do pin point calculations with your board"""
	pygame.draw.rect(Board_Screen, ORANGE, (Board_Width // 2 - 100, Board_Height // 2 - 60, 205, 50))
	Board_Screen.blit(end_img, (Board_Width // 2 - 100, Board_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board_Width // 2 - 80, Board_Height // 2 + 10))



def computerMove(AiTurn):
	global game_over 
	global winner
	Random_row = random.randint(0, 2) # random move in rows
	Random_colum = random.randint(0, 2) # random move in column

	"""Makes sure that if player 1 or player 2 wins 
	need this since after player 1 places doesn't matter if win or not ai will place a letter after
	if player wins make the winning move first but the ai does it counts ai as the winner that's"""
	for row in range(3):
		for colum in range(3):
			board_copy = copy.deepcopy(Board) 
			if board_copy[Random_row][Random_colum] == 0: 
				board_copy[Random_row][Random_colum] = AiTurn
				if Is_the_game_over() in board_copy:
					Ai_Board.append(draw_Letter())
					return board_copy

	"""Makes the Ai be able to move"""
	for row in range(3): # three rows
		for colum in range(3): # three colums
			board_copy = copy.deepcopy(Board) 
			if board_copy[Random_row][Random_colum] == 0: # chooses any location on board if it's open
				board_copy[Random_row][Random_colum] = AiTurn # Ai turn to go
				if Is_the_game_over() in board_copy: # is the game over in the ai board
					game_over = True
					winner = 2
				else: # if not continue add a letter until game is tied, player 1 wins or the ai wins 
					Ai_Board.append(draw_Letter())
					board_copy[Random_row][Random_colum] = AiTurn
					return board_copy

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
	for row in range(3): # 3 rows
		for colum in range(3): # 3 columns
			if Board[row][colum] == 0: # any spot with 0
				validMoves.append((colum, row)) # adds all aviable moves for the ai to move
	if len(validMoves) > 0: # if any spot is zero you can place a letter
		return random.choice(validMoves)
	else:
		return None	

"""Starts the game"""
def start_Ai_3by3_Board():
	"""access the variables outside the functions
	if you don't do this it doesn't work the way it should"""
	global winner
	global game_over
	global position
	global Board
	global Ai_Board
	global player
	global Mouse_clicked

	Start_Tic_Tac_Toe = True
	while Start_Tic_Tac_Toe == True:
	
		# draw board and ready for first click on board
		draw_board()
		draw_Letter()
		"""Opens the window and close window
		Closes the game when we press the X button in the window"""
		for window in pygame.event.get():
			if window.type == pygame.QUIT:
				Start_Tic_Tac_Toe = False
				
			"""for player 1 and player2 mouse clicks to be register on the board"""
			if game_over == False:
				if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
					Mouse_clicked = True
				if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
					Mouse_clicked = False
					position = pygame.mouse.get_pos()
					the_X_position = position[0] // 150
					The_Y_position = position[1] // 150
					if Board[the_X_position][The_Y_position] == 0: # place any letter if the spot is open
						Board[the_X_position][The_Y_position] = player # switch between player 1 and player 2
						if player == 1:
							Is_the_game_over()
							print(Board)
							if game_over == True:
								winner = 1
							else:
								player *= -1 # player 1 and player 2
						if player == -1:
							Board = computerMove(player)
							Is_the_game_over()
							print(Board)
							player *= -1

	
		# if someone has won the game or tied
		if game_over == True:
			draw_game_over(winner)
			# check for if we clicked on Play Again
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				position = pygame.mouse.get_pos()
				"""if player press play again resets everything"""
				if Play_Again_Box.collidepoint(position):
					game_over = False
					player = 1
					position = (0,0)
					Board = []
					winner = 0
					# creates empty 3 x 3 board again
					Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
					Ai_Board = []
		# update display
		pygame.display.update()
	
	pygame.quit()


start_Ai_3by3_Board()


