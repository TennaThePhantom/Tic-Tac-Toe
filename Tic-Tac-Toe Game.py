import pygame
from pygame.locals import * 
import sys
from board3by3 import *
from Board3by3ai import *
from Board4by4 import *
from Board4by4Ai import *
from Board5By5 import *
from Board5by5Ai import *
from Board6by6 import *
from Board7By7 import *
from Board10By10 import *
from StartMenu import *

pygame.init()

def tic_tac_toe_game_loop(): 
    Game_State = Game.Main_Menu
    Start_menu = True
    while Start_menu == True:
        if Game_State == Game.Main_Menu:
            Game_State = Title_screen(Menu_Screen)
        
        if Game_State == Game.Start_game_next_screen:
            Game_State = start_menu(Menu_Screen)

        if Game_State == Game.Help_screen:
            Game_State = Help_section(Menu_Screen)
        
        if Game_State == Game.How_to_play_3by3:
            Game_State = HowToPlay3X3Board(Menu_Screen)
        
        if Game_State ==  Game.How_to_play_5by5_or_more:
            Game_State = HowToPlay5X5BoardOrHigher(Menu_Screen)
        
        if Game_State == Game.Credits_screen:
            Game_State = credits_section(Menu_Screen)

        if Game_State == Game.Two_Player_mode:
            Game_State = Two_Player_Mode(Menu_Screen)

        if Game_State == Game.Ai_mode:
            Game_State = Ai_Mode(Menu_Screen)

        if Game_State == Game.QUIT:
            pygame.quit()
            return Start_menu == False

        if Game_State == Game.Board3by3:
            Game_State = pygame.display.set_mode((Board3X3_Width, Board3X3_Height))
            Game_State = pygame.display.set_caption('Tic-Tac-Toe 3X3 Board')
            start_3by3_Board()
        
    pygame.quit()
    sys.exit()

tic_tac_toe_game_loop()