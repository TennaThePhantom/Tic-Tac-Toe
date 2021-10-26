import pygame
from pygame import display
from pygame.locals import *



class Textformenu:

    def display_Text():

        # sizes 
        Start_Menu_Height = 675
        Start_Menu_Width = 800
        Message_X_Location = 400
        Message_Y_Location = 50

        The_Options_X = 400
        The_Options_Y = 370


        # colors
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)

        # Menu customization 
        Menu_Size = pygame.display.set_mode((Start_Menu_Width, Start_Menu_Height))
        pygame.display.set_caption("Tic-Tac-Toe Menu")
        Menu_Size.fill(BLACK)

        # text for screen
        Message_font = pygame.font.SysFont('Verdana', 30)
        Text_font = pygame.font.SysFont('Verdana', 50)
        Welcome_Message = Message_font.render('Welcome To Tic-Tac-Toe Main Menu',True, RED, BLACK)
        Start_Game = Text_font.render('Start Game', True, RED, BLACK)
        credits_Text = Text_font.render('Credits', True, RED, BLACK)
        Help_Text = Text_font.render('Help', True, RED, BLACK)

        Message = Welcome_Message.get_rect()
        Message.center = (Message_X_Location, Message_Y_Location)
        option1 = Start_Game.get_rect()
        option1.center = (The_Options_X, The_Options_Y)

        option2 = Help_Text.get_rect()
        option2.center = (The_Options_X, The_Options_Y + 90)

        option3 = credits_Text.get_rect()
        option3.center = (The_Options_X, The_Options_Y + 180)
        Menu_Size.blit(Welcome_Message, Message)
        Menu_Size.blit(Start_Game, option1)
        Menu_Size.blit(Help_Text, option2)
        Menu_Size.blit(credits_Text,option3)


