import pygame
from pygame.locals import *

pygame.init()

# the board
Board_Height = 600
Board_Width = 600
lines_width = 15
Board_Screen = pygame.display.set_mode((Board_Width, Board_Height))
pygame.display.set_caption('Tic Tac Toe 5 by 5 Board')

# colors to use
ROSE = (204, 0, 204)
ORANGE = (255, 153, 51)
DARK_BLUE = (0, 0, 204)
WHITE = (255, 255, 255)
# font type
font = pygame.font.SysFont(None, 100)

# variables for game
Mouse_clicked = False
player = 1
position = (0,0)
Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
game_over = False
winner = 0


# to play again 
again_rect = Rect(Board_Width // 2 - 160, Board_Height // 2, 400, 70)


def draw_board():
    background = (255, 255, 255)
    grid = (0, 0, 0)
    Board_Screen.fill(background)
    for Grid_Lines in range(1, 5): 
        """I got 120 from doing 600 / 5 since I'm having 5 rows and column"""
        pygame.draw.line(Board_Screen, grid, (0, 120 * Grid_Lines), (Board_Width, 120 * Grid_Lines), lines_width)
        pygame.draw.line(Board_Screen, grid, (120 * Grid_Lines, 0), (120 * Grid_Lines, Board_Height), lines_width)




def draw_letter():
    x_position = 0
    for spots in Board:
        y_position = 0
        for y in spots:
            if y == 1:
                pygame.draw.line(Board_Screen, ROSE, (x_position * 120 + 15, y_position * 120 + 15), (x_position * 120 + 105, y_position * 120 + 105), lines_width)
                pygame.draw.line(Board_Screen, ROSE, (x_position * 120 + 15, y_position * 120 + 105), (x_position * 120 + 105, y_position * 120 + 15), lines_width)
                """The first number 15 is where the line starts and
                the second number 105 is when the lines ends
                both combine have to equal whatever your board is divide 
                by the amount of rows you have"""
            if y == -1:
                """what's half of 120. 60 to place the circle in the middle of the box
                and the another number is the size of the circle
                you have to play around with that to get the size circle you want"""
                pygame.draw.circle(Board_Screen, ORANGE, (x_position * 120 + 60, y_position * 120 + 60), 52 , lines_width)
            y_position += 1
        x_position += 1



def Is_the_game_over():
    global game_over
    global winner

    x_position = 0

    for spots in Board:
        if sum(spots) == 5:
            winner = 1
            game_over = True
        if sum(spots) == -5:
            winner = 2
            game_over = True
        
        if Board[0][x_position] + Board[1][x_position] + Board[2][x_position] +  Board[3][x_position] + Board[4][x_position]  == 5:
            winner = 1
            game_over = True
        if Board[0][x_position] + Board[1][x_position] + Board[2][x_position] +  Board[3][x_position] + Board[4][x_position]  == -5:
            winner = 2
            game_over = True
        x_position += 1
    
    if Board[0][0] + Board[1][1] + Board [2][2] + Board[1][3] + Board [4][4] == 5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == 5:
        winner = 1
        game_over = True
    if Board[0][0] + Board[1][1] + Board [2][2] + Board[3][3] + Board [4][4] == -5 or Board[4][0] + Board[3][1] + Board[2][2] + Board[1][3] + Board[0][4] == -5:
        winner = 2
        game_over = True
    

    if game_over == False:
        tie = True
        for row in Board:
            for letter in row:
                if letter == 0:
                    tie = False
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
	Board_Screen.blit(Play_Again_IMG, (Board_Width // 2 - 180, Board_Height // 2 + 20))

def Start_5_by_5_Board():
    """Opens the window and close window"""
    global winner
    global game_over
    global position
    global Board
    global player
    global Mouse_clicked
    Start_Tic_Tac_Toe = True
    while Start_Tic_Tac_Toe == True:
        draw_board()
        draw_letter()
        for window in pygame.event.get():
            if window.type == pygame.QUIT:
                Start_Tic_Tac_Toe = False
            if game_over == False:

                if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
                    Mouse_clicked = True
                if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
                    Mouse_clicked = False
                    position = pygame.mouse.get_pos()
                    The_X_position = position[0] // 120
                    The_Y_position = position[1] // 120
                    if Board[The_X_position][The_Y_position] == 0:
                        Board[The_X_position][The_Y_position] = player
                        player *= -1
                        print(Board)
                        Is_the_game_over()

        if game_over == True:
            draw_game_over(winner)
            if window.type == pygame.MOUSEBUTTONDOWN and Mouse_clicked == False:
                Mouse_clicked = True
            if window.type == pygame.MOUSEBUTTONUP and Mouse_clicked == True:
                Mouse_clicked = False
                position = pygame.mouse.get_pos()
                if again_rect.collidepoint(position):
                    game_over = False
                    player = 1
                    position = (0, 0)
                    Board = []
                    winner = 0
                    Board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


        pygame.display.update()
        


Start_5_by_5_Board()
