import pygame
from pygame.locals import *


pygame.init()

Board_width_3X3_Ai = 450
Board_height_3X3_Ai = 450
lines_width = 15

Board_Screen = pygame.display.set_mode((Board_width_3X3_Ai, Board_height_3X3_Ai))

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)

Mouse_clicked = False
player = 1
position = (0,0)
Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
game_over = False
winner = 0

font = pygame.font.SysFont(None, 40)

def draw_board():
	BackGround = WHITE
	grid = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,3):
		"""I got 150 from doing 450 / 3 since I'm having 3 rows and column"""
		pygame.draw.line(Board_Screen, grid , (0, 150 * Grid_Lines), (Board_width_3X3_Ai,150 * Grid_Lines), lines_width)
		pygame.draw.line(Board_Screen, grid, (150 * Grid_Lines, 0), (150 * Grid_Lines, Board_height_3X3_Ai), lines_width)

def draw_Letter():
	x_position = 0
	for spots in Board:
		y_position = 0
		for player in spots:
			if player == 1: # player 1
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 25), (x_position * 150 + 125, y_position * 150 + 125), lines_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 125), (x_position * 150 + 125, y_position * 150 + 25), lines_width)
			if player == -1: # player 2
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 150 + 75, y_position * 150 + 75), 50, lines_width)
			y_position += 1
		x_position += 1	



def Start_AI_3X3():
	global winner
	global game_over
	global position
	global Board
	global player
	global Mouse_clicked
	Start_Ai = True
	while Start_Ai == True:
		draw_board()
		draw_Letter()

		for window in pygame.event.get():
			if window.type == pygame.QUIT:
				Start_Ai = False
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				"""for player 1 and player2 mouse clicks to be register on the board"""
				position = pygame.mouse.get_pos()
				the_X_position = position[0] // 150
				The_Y_position = position[1] // 150
				if Board[the_X_position][The_Y_position] == 0:
					Board[the_X_position][The_Y_position] = player
					player *= -1

		pygame.display.update()
	pygame.quit()



Start_AI_3X3()