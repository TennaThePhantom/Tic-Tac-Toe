import pygame
from pygame.locals import *
from StartMenu import *
from board3by3 import *
from Board4by4 import *
from Board5By5 import *
from Board6by6 import *
from Board7By7 import *
from Board10By10 import *
from Board3by3ai import *
from Board4by4Ai import * 
from Board5by5Ai import * 

pygame.init()

window_size = pygame.display.set_mode((800, 700))
pygame.display.update()



def Tic_Tac_toe_game():
    Game_State = Game.Main_Menu
    Start_Game = True
    while Start_Game == True:
        if Game_State == Game.Main_Menu:
            Game_State = Title_screen(Menu_Screen)

        if Game_State == Game.Start_game_next_screen:
            Game_State = start_menu(Menu_Screen)

        if Game_State == Game.Help_screen:
            Game_State = Help_section(Menu_Screen)

        if Game_State == Game.How_to_play_3by3:
            Game_State = HowToPlay3X3Board(Menu_Screen)

        if Game_State == Game.How_to_play_5by5_or_more:
            Game_State = HowToPlay5X5BoardOrHigher(Menu_Screen)

        if Game_State == Game.Credits_screen:
            Game_State = credits_section(Menu_Screen)

        if Game_State == Game.Two_Player_mode:
            Game_State = Two_Player_Mode(Menu_Screen)

        if Game_State == Game.Ai_mode:
            Game_State = Ai_Mode(Menu_Screen)

        if Game_State == Game.QUIT:
            pygame.quit()
        
        if Game_State == Game.Board3by3:
            Game_State = pygame.display.set_mode((Board3X3_Width, Board3X3_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')
            pygame.display.update()
            start_3by3_Board()
        
        if Game_State == Game.Board4by4:
            Game_State = pygame.display.set_mode((Board4X4_Width, Board4X4_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')
            pygame.display.update()
            start_4by4_Board()
        
        if Game_State == Game.Board5by5:
            Game_State = pygame.display.set_mode((Board5X5_Width, Board5X5_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 5X5 Board')
            pygame.display.update()
            start_5by5_Board()

        if Game_State == Game.Board6X6:
            Game_State = pygame.display.set_mode((Board6X6_Width, Board6X6_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 6X6 Board')
            pygame.display.update()
            start_6X6_board()
        
        if Game_State == Game.Board7By7:
            Game_State = pygame.display.set_mode((Board7X7_Width, Board7X7_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 7X7 Board')
            pygame.display.update()
            start_7X7_Board()
        
        if Game_State == Game.Board10By10:
            Game_State = pygame.display.set_mode((Board10X10_Width, Board10X10_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 10X10 Board')
            pygame.display.update()
            start_10X10_Board()
        
        if Game_State == Game.AiBoard_3by3:
            Game_State = pygame.display.set_mode((Ai_Board3X3_Width, Ai_Board3X3_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 3X3 Board")
            start_Ai_3by3_Board()

        if Game_State == Game.AiBoard_4by4:
            Game_State = pygame.display.set_mode((Ai_Board4X4_Width, Ai_Board4X4_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 4X4 Board")
            start_ai_4by4_Board()

                
        if Game_State == Game.Ai_Board5by5:
            Game_State = pygame.display.set_mode((Ai_Board5X5_Width, Ai_Board5X5_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 5X5 Board")
            start_ai_5by5_Board()
    
    pygame.display.update()

    
Tic_Tac_toe_game()
