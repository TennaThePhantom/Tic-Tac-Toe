import pygame
from pygame.locals import *
from StartMenu import *
from Board3by3 import *
from Board4by4 import *
from Board5By5 import *
from Board6by6 import *
from Board7By7 import *
from Board10By10 import *
from Board3by3Ai import *
from Board4by4Ai import * 
from Board5by5Ai import * 


"""Menu is connected to all boards"""
def tic_tac_toe_game():
    pygame.init()

    pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Tic-Tac-Toe Menu")

    Game_State = Game.Main_Menu
    Start_Game = True
    while Start_Game == True:
        """Menu"""
        if Game_State == Game.Main_Menu:
            Game_State = title_screen(Menu_Screen)

        if Game_State == Game.Start_Game_Next_Screen:
            Game_State = start_menu(Menu_Screen)

        if Game_State == Game.Help_Screen:
            Game_State = help_section(Menu_Screen)

        if Game_State == Game.How_To_Play_3By3:
            Game_State = how_to_play_3x3_board(Menu_Screen)

        if Game_State == Game.How_To_Play_4By4:
            Game_State = how_to_play_4x4_board(Menu_Screen)

        if Game_State == Game.How_To_Play_5By5_Or_More:
            Game_State = how_to_play_5x5_board_or_higher(Menu_Screen)

        if Game_State == Game.Credits_Screen:
            Game_State = credits_section(Menu_Screen)

        if Game_State == Game.Two_Player_Mode:
            Game_State = Two_Player_Mode(Menu_Screen)

        if Game_State == Game.Ai_Mode:
            Game_State = Ai_Mode(Menu_Screen)

        if Game_State == Game.QUIT:
            pygame.quit()
            sys.exit()

        """The boards for two player"""
        if Game_State == Game.Board3By3:
            Game_State = pygame.display.set_mode((Board3X3_Width, Board3X3_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')
            start_3x3_Board()
        
        if Game_State == Game.Board4By4:
            Game_State = pygame.display.set_mode((Board4X4_Width, Board4X4_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')
            start_4by4_board()
        
        if Game_State == Game.Board5By5:
            Game_State = pygame.display.set_mode((Ai_Board5X5_Height, Ai_Board5X5_Width))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 5X5 Board')
            start_ai_5by5_board()

        if Game_State == Game.Board6X6:
            Game_State = pygame.display.set_mode((Board6X6_Width, Board6X6_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 6X6 Board')
            start_6x6_board()
        
        if Game_State == Game.Board7By7:
            Game_State = pygame.display.set_mode((Board7X7_Width, Board7X7_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 7X7 Board')
            start_7x7_board()
        
        if Game_State == Game.Board10By10:
            Game_State = pygame.display.set_mode((Board10X10_Width, Board10X10_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 10X10 Board')
            start_10x10_board()
        
        """The boards for Ai"""
        if Game_State == Game.AiBoard_3By3:
            Game_State = pygame.display.set_mode((Ai_Board3X3_Width, Ai_Board3X3_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 3X3 Board")
            start_ai_3x3_board()

        if Game_State == Game.AiBoard_4By4:
            Game_State = pygame.display.set_mode((Ai_Board4X4_Width, Ai_Board4X4_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 4X4 Board")
            start_ai_4x4_board()

        if Game_State == Game.Ai_Board5By5:
            Game_State = pygame.display.set_mode((Ai_Board5X5_Width, Ai_Board5X5_Height))
            Game_State = pygame.display.set_caption("Ai Tic-Tac-Toe 5X5 Board")
            start_ai_5by5_board()
    
    pygame.display.update()

tic_tac_toe_game()


