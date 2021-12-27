#import modules
import pygame
from pygame.locals import *

pygame.init()

# the board dimensions
Board3X3_Height = 450
Board3X3_Width = 450
Lines_Width = 15
Board_Screen = pygame.display.set_mode((Board3X3_Width, Board3X3_Height))
pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')

# colors for board
ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# define font
Font = pygame.font.SysFont(None, 40)

# variables for game
Mouse_clicked = False
Player = 1
Position = (0,0)
Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Game_Over = False
Winner = 0

# draws a rectangle around play again 
Play_Again_Box = Rect(Board3X3_Width // 2 - 80, Board3X3_Height // 2, 160, 50)

# makes the board
def draw_board():
	BackGround = WHITE
	Grid_Lines_Color = BLACK
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,3):
		"""I got 150 from doing 450 / 3 since I'm having 3 rows and column"""
		pygame.draw.line(Board_Screen, Grid_Lines_Color , (0, 150 * Grid_Lines), (Board3X3_Width,150 * Grid_Lines), Lines_Width)
		pygame.draw.line(Board_Screen, Grid_Lines_Color, (150 * Grid_Lines, 0), (150 * Grid_Lines, Board3X3_Height), Lines_Width)

# makes X and O
def draw_Letter():
	X_Position = 0
	for Spots in Board:
		Y_Position = 0
		for Player in Spots:
			if Player == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 150 + 25, Y_Position * 150 + 25), (X_Position * 150 + 125, Y_Position * 150 + 125), Lines_Width)
				pygame.draw.line(Board_Screen, ROSE, (X_Position * 150 + 25, Y_Position * 150 + 125), (X_Position * 150 + 125, Y_Position * 150 + 25), Lines_Width)
				"""The first number 25 is where the line starts and
					the second number 125 is when the lines ends
					both combine have to equal whatever your board is divide 
					by the amount of rows you have"""
			if Player == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (X_Position * 150 + 75, Y_Position * 150 + 75), 50, Lines_Width)
			"""What's half of 150. 75 to place the circle in the middle of the box
			and the other number is the size of the circle
			you have to play around with that to get the circle size you want"""
			Y_Position += 1
		X_Position += 1	

"""Checks the board if player 1 or 2 have won or is it a tie game"""
def Is_the_game_over():
	# acesss variables outside the function
	global Game_Over
	global Winner

	Letter = 0
	for spots in Board:
		# checks column for 3 in a row
		if sum(spots) == 3: # when player 1 place a letter it's + 1
			Winner = 1
			Game_Over = True
		if sum(spots) == -3: # when player place a letter it's - 1
			Winner = 2
			Game_Over = True
		# checks for 3 in a row 
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == 3:
			Winner = 1
			Game_Over = True
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == -3:
			Winner = 2
			Game_Over = True
		Letter += 1

	# checks for 3 in a row diagonal 
	if Board[0][0] + Board[1][1] + Board[2][2] == 3 or Board[2][0] + Board[1][1] + Board[0][2] == 3:
		Winner = 1
		Game_Over = True
	if Board[0][0] + Board[1][1] + Board[2][2] == -3 or Board[2][0] + Board[1][1] + Board[0][2] == -3:
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

"""Makes the text when game is over or tie game"""
def draw_game_over_text(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = Font.render(end_text, True, DARK_BLUE)
	"""Either play around with draw.rect and blit for this part or do pin point calculations with your board"""
	pygame.draw.rect(Board_Screen, ORANGE, (Board3X3_Width // 2 - 100, Board3X3_Height // 2 - 60, 205, 50))
	Board_Screen.blit(end_img, (Board3X3_Width // 2 - 100, Board3X3_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = Font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, Play_Again_Box)
	Board_Screen.blit(Play_Again_IMG, (Board3X3_Width // 2 - 80, Board3X3_Height // 2 + 10))

"""Starts the game"""
def start_3by3_Board():
	"""Access the variables outside the functions.
	Need this or it won't work the way it should"""
	global Winner
	global Game_Over
	global Position
	global Board
	global Player
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
			"""For player 1 and player2 mouse clicks to be register on the board"""
			if Game_Over == False:
				if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
					Mouse_clicked = True
				if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
					Mouse_clicked = False
					Position = pygame.mouse.get_pos()
					the_X_position = Position[0] // 150
					The_Y_position = Position[1] // 150
					if Board[the_X_position][The_Y_position] == 0:
						Board[the_X_position][The_Y_position] = Player
						Is_the_game_over()
						print(Board)
						Player *= -1 # swap turns
		# if someone has won the game or tied
		if Game_Over == True:
			draw_game_over_text(Winner)
			# check for if we clicked on Play Again
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				Position = pygame.mouse.get_pos()
				"""If player press play again resets everything"""
				if Play_Again_Box.collidepoint(Position):
					Game_Over = False
					Player = 1
					Position = (0,0)
					Board = []
					Winner = 0
					# creates empty 3 x 3 board again
					Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		# update display
		pygame.display.update()

	pygame.quit()


start_3by3_Board()


