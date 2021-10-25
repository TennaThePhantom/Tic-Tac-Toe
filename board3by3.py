#import modules
import pygame
from pygame.locals import *

pygame.init()

Board_Height = 450
Board_Width = 450
line_width = 10
Board_Screen = pygame.display.set_mode((Board_Width, Board_Height))
pygame.display.set_caption('Tic Tac Toe')

# colors
ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)

# define font
font = pygame.font.SysFont(None, 40)

#define variables
Mouse_clicked = False
player = 1
position = (0,0)
Board = []
game_over = False
winner = 0

#setup a rectangle for "Play Again" Option
again_rect = Rect(Board_Width // 2 - 80, Board_Height // 2, 160, 50)

#create empty 3 x 3 list to represent the grid
for spots in range (3):
	row = [0] * 3
	Board.append(row)



def draw_board():
	BackGround = (255, 255, 255)
	grid = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,3):
		pygame.draw.line(Board_Screen, grid, (0, 150 * Grid_Lines), (Board_Width,150 * Grid_Lines), line_width)
		pygame.draw.line(Board_Screen, grid, (150 * Grid_Lines, 0), (150 * Grid_Lines, Board_Height), line_width)

def draw_Letter():
	x_position = 0
	for spots in Board:
		y_position = 0
		for y in spots:
			if y == 1:
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 25), (x_position * 150 + 125, y_position * 150 + 125), line_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 125), (x_position * 150 + 125, y_position * 150 + 25), line_width)
			if y == -1:
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 150 + 75, y_position * 150 + 75), 50, line_width)
			y_position += 1
		x_position += 1	


def check_game_over():
	global game_over
	global winner

	x_position = 0
	for spots in Board:
		#check columns
		if sum(spots) == 3:
			winner = 1
			game_over = True
		if sum(spots) == -3:
			winner = 2
			game_over = True
		#check rows
		if Board[0][x_position] + Board [1][x_position] + Board [2][x_position] == 3:
			winner = 1
			game_over = True
		if Board[0][x_position] + Board [1][x_position] + Board [2][x_position] == -3:
			winner = 2
			game_over = True
		x_position += 1

	#check cross
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
		#if it is a tie, then call game over and set winner to 0 (no one)
		if tie == True:
			game_over = True
			winner = 0



def draw_game_over(winner):

	if winner != 0:
		end_text = "Player " + str(winner) + " wins!"
	elif winner == 0:
		end_text = "You have tied!"

	end_img = font.render(end_text, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, (Board_Width // 2 - 150, Board_Height // 2 - 60, 200, 50))
	Board_Screen.blit(end_img, (Board_Width // 2 - 150, Board_Height // 2 - 50))

	Play_Again = 'Play Again?'
	Play_Again_IMG = font.render(Play_Again, True, DARK_BLUE)
	pygame.draw.rect(Board_Screen, ORANGE, again_rect)
	Board_Screen.blit(Play_Again_IMG, (Board_Width // 2 - 80, Board_Height // 2 + 10))


# GUI Loop
Start_Tic_Tac_Toe = True
while Start_Tic_Tac_Toe:

	# draw board and ready for first click on board
	draw_board()
	draw_Letter()

	# all the main things for GUI to work
	for window in pygame.event.get():
		#handle game exit
		if window.type == pygame.QUIT:
			Start_Tic_Tac_Toe = False
		#Starts new game
		if game_over == False:
			#check for mouseclick
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				position = pygame.mouse.get_pos()
				the_X_position = position[0] // 150
				The_Y_position = position[1] // 150
				if Board[the_X_position][The_Y_position] == 0:
					Board[the_X_position][The_Y_position] = player
					player *= -1
					check_game_over()

	# if game someone has won the game
	if game_over == True:
		draw_game_over(winner)
		# check for if we clicked on Play Again
		if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
			Mouse_clicked = True
		if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
			Mouse_clicked = False
			position = pygame.mouse.get_pos()
			if again_rect.collidepoint(position):
				# resets everything
				game_over = False
				player = 1
				position = (0,0)
				Board = []
				winner = 0
				#create empty 3 x 3 list to represent the grid
				for spots in range (3):
					row = [0] * 3
					Board.append(row)

	#update display
	pygame.display.update()

pygame.quit()
