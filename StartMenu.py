import pygame
import pygame.freetype
import sys
from pygame.sprite import Sprite
from enum import Enum

pygame.init()

DARK_PURPLE = (102, 0, 102)
LIGHT_BLUE = (0, 255, 255)

Menu_Screen = pygame.display.set_mode((800, 700))
pygame.display.update()


def make_a_place_on_screen_for_text(text, Text_Size, Text_Color, Bg_rgb):
    """ display's text on screen"""
    Font = pygame.freetype.SysFont("Verdana", Text_Size, bold=True)
    Surface, _ = Font.render(text=text, fgcolor=Text_Color, bgcolor=Bg_rgb)
    return Surface.convert_alpha()

def display_regular_text(Text,Text_Size, Text_X, Text_Y,Text_color, Bg_Color):
    """Non Interactive text"""
    Font = pygame.font.SysFont("Verdana",Text_Size, bold=True)
    text = Font.render(Text, True, Text_color, Bg_Color)
    Text_Box = text.get_rect() # makes box for text
    Text_Box.center = (Text_X, Text_Y) # X and Y location 
    Menu_Screen.blit(text, Text_Box) # displays text on screen

def help_with_3By3_board_text():
    display_regular_text("How to play 3 By 3 board", 30, 400, 50, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Player 1 is always X ", 25, 400, 100, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Click on the box to place a letter", 30, 400, 150, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Your goal is to get 3 in a row", 30, 400, 200, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If you get 3 in a row (Up, Down, Across, or Diagonally) ", 25, 400, 250, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You win the game ", 25, 400, 280, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If the person or the computer place a letter in a box", 25, 400, 330, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You cannot place your letter in that box anymore", 25, 400, 360, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If all 9 boxes have been fulled up", 25, 400, 410, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("The game ends in a tie", 25, 400, 440, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Nobody wins the game ", 25, 400, 470, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Have fun playing Tic-Tac-Toe ", 25, 400, 520, LIGHT_BLUE, DARK_PURPLE)


def help_with_4By4_board_text():
    display_regular_text("How to play 4 By 4 board", 30, 400, 50, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Player 1 is always X ", 25, 400, 100, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Click on the box to place a letter", 30, 400, 150, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Your goal is to get 4 in a row", 30, 400, 200, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If you get 4 in a row (Up, Down, Across, or Diagonally) ", 25, 400, 250, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You win the game ", 25, 400, 280, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If the person or the computer place a letter in a box", 25, 400, 330, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You cannot place your letter in that box anymore", 25, 400, 360, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If all 16 boxes have been fulled up", 25, 400, 410, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("The game ends in a tie", 25, 400, 440, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Nobody wins the game ", 25, 400, 470, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Have fun playing Tic-Tac-Toe ", 25, 400, 520, LIGHT_BLUE, DARK_PURPLE)


def help_with_5By5_board_or_higher_text():
    display_regular_text("How to play 5 By 5 board or higher", 30, 400, 50, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Player 1 is Always X", 30, 400, 100, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Click on the box to place a letter", 30, 400, 150, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Make sure you click the right box", 30, 400, 190, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Bigger board smaller boxes", 30, 400, 230, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If you get 5 in a row (Up, Down, Across, or Diagonally) ", 25, 400, 280, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You win the game", 25, 400, 315, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If the person or the computer place a letter in a box", 25, 400, 350, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("You cannot place your letter in that box anymore", 25, 400, 390, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("If all boxes have been fulled up", 25, 400, 430, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("The game ends in a tie", 25, 400, 460, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Nobody wins the game ", 25, 400, 495, LIGHT_BLUE, DARK_PURPLE)
    display_regular_text("Have fun playing Tic-Tac-Toe", 25, 400, 550, LIGHT_BLUE, DARK_PURPLE)


class Reactive_Text(Sprite):
    def __init__(self, Text_Center, text, Text_Size, Bg_rgb, Text_color, Action=None):
        self.Mouse_Over = False  # Is the mouse over the text?

        # Creates the regular text
        Default_Text = make_a_place_on_screen_for_text(
            text=text, Text_Size=Text_Size, Text_Color=Text_color, Bg_rgb=Bg_rgb
        )

        # creates the reactive text
        Highlighted_Text = make_a_place_on_screen_for_text(
            text=text, Text_Size=Text_Size * 1.2, Text_Color=Text_color, Bg_rgb=Bg_rgb
        )

        # both the reactive and Regular text are now one
        self.High_lights_text = [Default_Text, Highlighted_Text]
        self.Reactive = [
            Default_Text.get_rect(center=Text_Center),
            Highlighted_Text.get_rect(center=Text_Center),
        ]
        # for text to do some type of command or action
        self.Action = Action

        # calls the init method of the parent sprite class
        super().__init__()

    """ is the mouse over text if yes does reactive if no goes to regular text """
    @property
    def Default(self):
        return self.High_lights_text[1] if self.Mouse_Over else self.High_lights_text[0]

    @property
    def TextReactive(self):
        return self.Reactive[1] if self.Mouse_Over else self.Reactive[0]

    def update(self, mouse_postition, mouse_over):

        if self.TextReactive.collidepoint(mouse_postition):
            self.Mouse_Over = True
            if mouse_over:
                return self.Action
        else:
            self.Mouse_Over = False

        """ Places the text onto menu """
    def place_text(self, surface):
        surface.blit(self.Default, self.TextReactive)


class Game(Enum):
    Main_Menu = 0
    Start_Game_Next_Screen = 1
    QUIT = -1
    Help_Screen = 2
    Credits_Screen = -2
    Two_Player_Mode = 3
    Ai_Mode = -3

    How_To_Play_3By3 = 4
    How_To_Play_4By4 = -4
    How_To_Play_5By5_Or_More = 5

    Board3By3 = 6
    AiBoard_3By3 = -6
    Board4By4 = 7
    AiBoard_4By4 = -7
    Board5By5 = 8
    Ai_Board5By5 = -8
    Board6X6 = 9
    Board7By7 = -9
    Board10By10 = 10


"""Text for menu screen"""
def title_screen(MenuScreen):

    Start_Game_Text = Reactive_Text(
    Text_Center = (400, 300),
    Text_Size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text ="Start Game",
    Action = Game.Start_Game_Next_Screen, 
    )
    Help_Text = Reactive_Text(
    Text_Center = (400, 400),
    Text_Size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Help",
    Action = Game.Help_Screen
    )
    Credits_Text = Reactive_Text(
    Text_Center = (400, 500),
    Text_Size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Credits",
    Action = Game.Credits_Screen
    )
    Quit_Text = Reactive_Text(
    Text_Center = (400, 600),
    Text_Size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Quit",
    Action = Game.QUIT,
    )

    Text_For_Menu = [Start_Game_Text, Help_Text, Credits_Text ,Quit_Text]
    Menu = True
    while Menu == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        MenuScreen.fill(DARK_PURPLE)
        display_regular_text("Tic-Tac-Toe", 45, 400, 50, LIGHT_BLUE,DARK_PURPLE)

        for Text in Text_For_Menu:
            Menu_Action = Text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Menu_Action is not None:
                return Menu_Action
            Text.place_text(MenuScreen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


"""When you hit start game goes to next screen"""
def start_menu(Menu_Screen):

    Menu_Return = True
    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )
    Two_player_Text = Reactive_Text(
    Text_Center = (400, 300),
    Text_Size = 50,
    Bg_rgb = DARK_PURPLE, 
    Text_color = LIGHT_BLUE, 
    text = "Two Player",
    Action = Game.Two_Player_Mode
    )
    Vs_Ai_text = Reactive_Text(
    Text_Center = (400, 500),
    Text_Size = 50,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Ai",
    Action = Game.Ai_Mode
    )

    Text = [Two_player_Text, Vs_Ai_text, Return_Back_To_Screen]
    while Menu_Return == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How do you want to play?", 40, 400, 50, LIGHT_BLUE, DARK_PURPLE)
        
        for Every_Text in Text:
            Second_Screen = Every_Text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Second_Screen is not None:
                return Second_Screen
            Every_Text.place_text(Menu_Screen)
            
        pygame.display.flip()

    pygame.quit()
    sys.exit()

def help_section(Menu_Screen):

    How_To_Play_3By3 = Reactive_Text(
    Text_Center = (400, 200),
    Text_Size = 50,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "3 By 3 Board",
    Action = Game.How_To_Play_3By3
    )
    How_To_Play_4By4 = Reactive_Text(
    Text_Center = (400, 400),
    Text_Size = 50,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "4 By 4 Board",
    Action = Game.How_To_Play_4By4
    )
    How_To_Play_5By5_Or_Higher = Reactive_Text(
    Text_Center = (400, 600),
    Text_Size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board or Higher",
    Action = Game.How_To_Play_5By5_Or_More
    )
    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )

    Text_for_help_section = [How_To_Play_3By3, How_To_Play_4By4 ,How_To_Play_5By5_Or_Higher, Return_Back_To_Screen]
    Help_section_display = True
    while Help_section_display == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How to play?", 40, 400, 50, LIGHT_BLUE, DARK_PURPLE )

        for Every_text in Text_for_help_section:
            Help_section_screen = Every_text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Help_section_screen is not None:
                return Help_section_screen
            Every_text.place_text(Menu_Screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def how_to_play_3x3_board(Menu_Screen):

    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to help screen",
    Action = Game.Help_Screen
    )
    Return_Back_To_Help_Screen = Reactive_Text(
    Text_Center = (615, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu
)

    Return_Back = [Return_Back_To_Screen, Return_Back_To_Help_Screen]
    Display_Text = True
    while Display_Text == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        help_with_3By3_board_text()

        for text in Return_Back:
            Go_Back = text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Go_Back is not None:
                return Go_Back
            text.place_text(Menu_Screen)

        pygame.display.flip()

def how_to_play_4x4_board(Menu_Screen):

    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to help screen",
    Action = Game.Help_Screen
    )
    Return_Back_To_Help_Screen = Reactive_Text(
    Text_Center = (615, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu
)

    Return_Back = [Return_Back_To_Screen, Return_Back_To_Help_Screen]
    Display_Text = True
    while Display_Text == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        help_with_4By4_board_text()

        for text in Return_Back:
            Go_Back = text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Go_Back is not None:
                return Go_Back
            text.place_text(Menu_Screen)

        pygame.display.flip()


def how_to_play_5x5_board_or_higher(Menu_Screen):

    Return_Back_To_Screen_Help_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to help screen",
    Action = Game.Help_Screen
    )

    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (615, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu
    )
    Return_Back = [Return_Back_To_Screen_Help_Screen, Return_Back_To_Screen]
    Display_Text = True
    while Display_Text == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        help_with_5By5_board_or_higher_text()

        for Text in Return_Back:
            Go_Back_To_Help_Section = Text.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Go_Back_To_Help_Section is not None:
                return Go_Back_To_Help_Section
            Text.place_text(Menu_Screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def credits_section(Menu_Screen):

    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )
    Text_To_Return = [Return_Back_To_Screen]
    Credits_Display = True
    while Credits_Display == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Credits", 50, 400, 300, LIGHT_BLUE, DARK_PURPLE)
        display_regular_text("Made By Tennessee Foster", 45, 400, 350, LIGHT_BLUE, DARK_PURPLE)

        for Text in Text_To_Return:
            Return_Back = Return_Back_To_Screen.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Return_Back is not None:
                return Return_Back
            Text.place_text(Menu_Screen)

        pygame.display.flip()
    
    pygame.quit()
    sys.exit()


def Two_Player_Mode(Menu_Screen):

    Board_Size_3X3 = Reactive_Text(
    Text_Center = (400, 200),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "3 By 3 Board",
    Action = Game.Board3By3
    )
    Board_Size_4X4 = Reactive_Text(
    Text_Center = (400, 280),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "4 By 4 Board",
    Action = Game.Board4By4
    )
    Board_Size_5X5 = Reactive_Text(
    Text_Center = (400, 360),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board",
    Action = Game.Board5By5
    )
    Board_Size_6X6 = Reactive_Text(
    Text_Center = (400, 440),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "6 By 6 Board",
    Action = Game.Board6X6
    )
    Board_Size_7X7 = Reactive_Text(
    Text_Center = (400, 520),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "7 By 7 Board",
    Action = Game.Board7By7
    )
    Board_Size_10X10 = Reactive_Text(
    Text_Center = (400, 600),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "10 By 10 Board",
    Action = Game.Board10By10
    )
    Return_Back_To_Game_Mode = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to game menu",
    Action = Game.Start_Game_Next_Screen,
    )
    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (615, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )

    Board_Sizes = [Board_Size_3X3,Board_Size_5X5, Board_Size_7X7,
    Board_Size_10X10, Board_Size_4X4, Board_Size_6X6, Return_Back_To_Game_Mode, Return_Back_To_Screen ]
    Choose_Board_Size = True

    while Choose_Board_Size == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Choose Your Board", 40, 400, 50, LIGHT_BLUE,DARK_PURPLE)

        for Every_Board_Size in Board_Sizes:
            Boards = Every_Board_Size.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Boards is not None:
                return Boards
            Every_Board_Size.place_text(Menu_Screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def Ai_Mode(Menu_Screen):

    Board_Size_3X3 = Reactive_Text(
    Text_Center = (400, 200),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "3 By 3 Board",
    Action = Game.AiBoard_3By3
    )
    Board_Size_4X4 = Reactive_Text(
    Text_Center = (400, 360),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "4 By 4 Board",
    Action = Game.AiBoard_4By4
    )
    Board_Size_5X5 = Reactive_Text(
    Text_Center = (400, 520),
    Text_Size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board",
    Action = Game.Ai_Board5By5
    )
    Return_Back_To_Screen_Game_Mode = Reactive_Text(
    Text_Center = (190, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to game mode",
    Action = Game.Start_Game_Next_Screen,
    )
    Return_Back_To_Screen = Reactive_Text(
    Text_Center = (615, 670),
    Text_Size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )

    Board_Sizes = [Board_Size_3X3,Board_Size_4X4, Board_Size_5X5,
    Return_Back_To_Screen_Game_Mode, Return_Back_To_Screen ]
    Choose_Board_Size = True

    while Choose_Board_Size == True:
        Mouse_Over_Text = False
        for Window in pygame.event.get():
            if Window.type == pygame.MOUSEBUTTONUP and Window.button == 1:
                Mouse_Over_Text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Choose Your Board", 40, 400, 50, LIGHT_BLUE,DARK_PURPLE)

        for Every_board_Size in Board_Sizes:
            Boards = Every_board_Size.update(pygame.mouse.get_pos(), Mouse_Over_Text)
            if Boards is not None:
                return Boards
            Every_board_Size.place_text(Menu_Screen)

        pygame.display.flip()
        
    pygame.quit()
    sys.exit()



