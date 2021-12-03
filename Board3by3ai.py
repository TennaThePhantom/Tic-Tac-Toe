import pygame
import copy
import random
from pygame.locals import *

pygame.init()

Board_Height = 450
Board_Width = 450
line_width = 15

Board_Screen = pygame.display.set_mode((Board_Width, Board_Height))
pygame.display.set_caption('Tic Tac Toe 3X3 Board')

ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)


font = pygame.font.SysFont(None, 40)

Mouse_clicked = False
player = 1
position = (0,0)
Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Ai_Board = []
game_over = False
winner = 0

Play_Again_Box = Rect(Board_Width // 2 - 80, Board_Height // 2, 160, 50)



def draw_board():
	BackGround = WHITE
	grid = (0, 0, 0)
	Board_Screen.fill(BackGround)
	for Grid_Lines in range(1,3):
		pygame.draw.line(Board_Screen, grid , (0, 150 * Grid_Lines), (Board_Width,150 * Grid_Lines), line_width)
		pygame.draw.line(Board_Screen, grid, (150 * Grid_Lines, 0), (150 * Grid_Lines, Board_Height), line_width)

def draw_Letter():
	x_position = 0
	for spots in Board:
		y_position = 0
		for player in spots:
			if player == 1: 
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 25), (x_position * 150 + 125, y_position * 150 + 125), line_width)
				pygame.draw.line(Board_Screen, ROSE, (x_position * 150 + 25, y_position * 150 + 125), (x_position * 150 + 125, y_position * 150 + 25), line_width)
			if player == -1: 
				pygame.draw.circle(Board_Screen, ORANGE, (x_position * 150 + 75, y_position * 150 + 75), 50, line_width)
			y_position += 1
		x_position += 1	

def Is_the_game_over():
	global game_over
	global winner

	Letter = 0
	for spots in Board:
		if sum(spots) == 3: 
			winner = 1
			game_over = True
		if sum(spots) == -3: 
			winner = 2
			game_over = True
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == 3:
			winner = 1
			game_over = True
		if Board[0][Letter] + Board [1][Letter] + Board [2][Letter] == -3:
			winner = 2
			game_over = True
		Letter += 1

	if Board[0][0] + Board[1][1] + Board [2][2] == 3 or Board[2][0] + Board[1][1] + Board [0][2] == 3:
		winner = 1
		game_over = True
	if Board[0][0] + Board[1][1] + Board [2][2] == -3 or Board[2][0] + Board[1][1] + Board [0][2] == -3:
		winner = 2
		game_over = True

	if game_over == False:
		tie = True
		for row in Board:
			for Zero in row:
				if Zero == 0:
					tie = False
		if tie == True:
			game_over = True
			winner = 0

def computerMove(AiTurn):
	global game_over 
	global winner
	for i in range(3):
		for j in range(3):
			board_copy = copy.deepcopy(Board)
			if board_copy[i][j] == 0:
				board_copy[i][j] = AiTurn
				if Is_the_game_over() in board_copy:
					game_over = True
					winner = 2
				elif AiTurn == -1:
					Ai_Board.append(draw_Letter())
					return board_copy
	turn = AiTurn * -1
	for i in range(3):
		for j in range(3):
			board_copy = copy.deepcopy(Board)
			if board_copy[i][j] == 0:
				board_copy[i][j] = turn
				if Is_the_game_over() in board_copy:
					game_over = True
					winner = 2
				elif AiTurn == -1:
					Ai_Board.append(draw_Letter())
					return board_copy

	move = make_the_ai_move()
	if move != None:
		x, y = move
		board_copy = copy.deepcopy(Board)
		board_copy[y][x] = AiTurn
		if AiTurn == -1:
			Ai_Board.append(draw_Letter())
			return board_copy
	return Board


def make_the_ai_move():
	VaildMoves = []
	for i in range(3):
		for j in range(3):
			if Board[i][j] == 0:
				VaildMoves.append((j,i))
	if len(VaildMoves) > 0:
		return random.choice(VaildMoves)
	else:
		return None


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

def start_3by3_Board():
	global winner
	global game_over
	global position
	global Board
	global player
	global Mouse_clicked

	Start_Tic_Tac_Toe = True
	while Start_Tic_Tac_Toe == True:
	
		draw_board()
		draw_Letter()
		for window in pygame.event.get():
			if window.type == pygame.QUIT:
				Start_Tic_Tac_Toe = False
				
			if game_over == False:
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
						Is_the_game_over()
						if player == -1:
							Board = computerMove(player)
							print(Board)
							player *= -1
							Is_the_game_over()

	
		if game_over == True:
			draw_game_over(winner)
			if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
				Mouse_clicked = True
			if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
				Mouse_clicked = False
				position = pygame.mouse.get_pos()
				if Play_Again_Box.collidepoint(position):
					game_over = False
					player = 1
					position = (0,0)
					Board = []
					winner = 0
					Board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		pygame.display.update()
	
	pygame.quit()


start_3by3_Board()


