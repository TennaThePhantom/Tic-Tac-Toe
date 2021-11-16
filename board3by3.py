#import modules
import pygame
from pygame.locals import *

pygame.init()

# the board
Board_Height = 450
Board_Width = 450
line_width = 10

Board_Screen = pygame.display.set_mode((Board_Width, Board_Height))
pygame.display.set_caption('Tic Tac Toe')

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
game_over = False
winner = 0

# draws a rectangle around play again 
again_rect = Rect(Board_Width // 2 - 80, Board_Height // 2, 160, 50)



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
		for y in spots:
			if y == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 25), (x_position * 150 + 125, y_position * 150 + 125), line_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 125), (x_position * 150 + 125, y_position * 150 + 25), line_width)
				"""The first number 25 is where the line starts and
					the second number 15 is when the lines ends
					both combine have to equal whatever your board is divide 
					by the amount of rows you have"""
			if y == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 150 + 75, y_position * 150 + 75), 50, line_width)
			"""what's half of 150. 75 to place the circle in the middle of the box
			and the another number is the size of the circle
			you have to play around with that to get the size circle you want"""
			y_position += 1
		x_position += 1	

"""Checks the board if player 1 or 2 have won or is it a tie game(is the board full)"""
def Is_the_game_over():
	# acesss variables outside the function
	global game_over
	global winner

	Y_position = 0
	for spots in Board:
		# checks column for 3 in a row
		if sum(spots) == 3: # when you place a letter it's + 1
			winner = 1
			game_over = True
		if sum(spots) == -3: # when you place a letter it's - 1
			winner = 2
			game_over = True
		# checks 3 in a row 
		if Board[0][Y_position] + Board [1][Y_position] + Board [2][Y_position] == 3:
			winner = 1
			game_over = True
		if Board[0][Y_position] + Board [1][Y_position] + Board [2][Y_position] == -3:
			winner = 2
			game_over = True
		Y_position += 1

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
			for letter in row:
				if letter == 0:
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
	pygame.draw.rect(Board_Screen, ORANGE, again_rect)
	Board_Screen.blit(Play_Again_IMG, (Board_Width // 2 - 80, Board_Height // 2 + 10))

"""Starts the game"""
def start_3by3_Board():
	"""access the variables outside the functions"""
	global winner
	global game_over
	global position
	global Board
	global player
	global Mouse_clicked

	Start_Tic_Tac_Toe = True
	while Start_Tic_Tac_Toe:
	
		# draw board and ready for first click on board
		draw_board()
		draw_Letter()
		"""Opens the window and close window"""
		for window in pygame.event.get():
			if window.type == pygame.QUIT:
				Start_Tic_Tac_Toe = False
			if game_over == False:
				"""Closes the game when we press the X button in the window"""
				if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
					Mouse_clicked = True
				if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
					Mouse_clicked = False
					"""for player 1 and player2 mouse clicks to be rezgtaurd on the board"""
					position = pygame.mouse.get_pos()
					the_X_position = position[0] // 150
					The_Y_position = position[1] // 150
					if Board[the_X_position][The_Y_position] == 0:
						Board[the_X_position][The_Y_position] = player
						player *= -1
						print(Board)
						Is_the_game_over()

	
		# if someone has won the game
		if game_over == True:
			draw_game_over(winner)
			# check for if we clicked on Play Again
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				position = pygame.mouse.get_pos()
				"""if player press play again resets everything"""
				if again_rect.collidepoint(position):
					game_over = False
					player = 1
					position = (0,0)
					Board = []
					winner = 0
					# creates empty 3 x 3 board again if you want to play again
					Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		# update display
		pygame.display.update()
	
	pygame.quit()


