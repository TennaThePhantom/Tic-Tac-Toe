import pygame
import pygame.freetype
from pygame.sprite import Sprite
from enum import Enum


DARK_PURPLE = (102, 0, 102)
LIGHT_BLUE = (0, 255, 255)
Menu_Screen = pygame.display.set_mode((800, 700))

pygame.display.set_caption("Tic-Tac-Toe Menu")

def Make_a_place_on_screen_for_text(text, Text_size, Text_Color, Bg_rgb):
    """ display's text on screen"""
    font = pygame.freetype.SysFont("Verdana", Text_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=Text_Color, bgcolor=Bg_rgb)
    return surface.convert_alpha()

def display_regular_text(Text,Text_size, Text_X, Text_Y,Text_color, Bg_Color):
    """Non Interactive text"""
    font = pygame.font.SysFont("Verdana",Text_size, bold=True)
    text = font.render(Text, True, Text_color, Bg_Color)
    Text_Box = text.get_rect() # makes box for text
    Text_Box.center = (Text_X, Text_Y) # X and Y location 
    Menu_Screen.blit(text, Text_Box) # displays text on screen



class Recative_Text(Sprite):
    """Makes the text be able to react"""
    def __init__(self, Text_Center, text, Text_size, Bg_rgb, Text_color, Action=None):
        self.mouse_over = False  # Is the mouse over the text?

        # Creates the regular text
        default_Text = Make_a_place_on_screen_for_text(
            text=text, Text_size=Text_size, Text_Color=Text_color, Bg_rgb=Bg_rgb
        )

        # creates the reactive text
        highlighted_Text = Make_a_place_on_screen_for_text(
            text=text, Text_size=Text_size * 1.2, Text_Color=Text_color, Bg_rgb=Bg_rgb
        )

        # both the reactive and Regular text are now one
        self.High_lights_text = [default_Text, highlighted_Text]
        self.Reactive = [
            default_Text.get_rect(center=Text_Center),
            highlighted_Text.get_rect(center=Text_Center),
        ]
        # for text to do some type of command or action
        self.Action = Action

        # calls the init method of the parent sprite class
        super().__init__()

    """ is the mouse over text if yes does reactive if no goes to regular text """
    @property
    def default(self):
        return self.High_lights_text[1] if self.mouse_over else self.High_lights_text[0]

    @property
    def TextReactive(self):
        return self.Reactive[1] if self.mouse_over else self.Reactive[0]

    def update(self, mouse_postition, mouse_over):

        if self.TextReactive.collidepoint(mouse_postition):
            self.mouse_over = True
            if mouse_over:
                return self.Action
        else:
            self.mouse_over = False

        """ Places the text onto menu """
    def Place_Text(self, surface):
        surface.blit(self.default, self.TextReactive)


class Game(Enum):
    QUIT = -1
    Main_Menu = 0
    Start_game_next_screen = 1
    Help_screen = 2
    Credits_screen = -2
    Two_Player_mode = 3
    Ai_mode = -3
    How_to_play_3by3 = 4
    How_to_play_5by5_or_more = -4


# the main loop
def menu_loop():

    pygame.init()

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
            return


"""Text for menu screen"""
def Title_screen(MenuScreen):

    Start_Game_Text = Recative_Text(
    Text_Center = (400, 300),
    Text_size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text ="Start Game",
    Action = Game.Start_game_next_screen, 
    )
    Help_Text = Recative_Text(
        Text_Center = (400, 400),
        Text_size = 45,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Help",
        Action = Game.Help_screen
    )
    credits_Text = Recative_Text(
        Text_Center = (400, 500),
        Text_size = 45,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Credits",
        Action = Game.Credits_screen
    )
    quit_Text = Recative_Text(
        Text_Center = (400, 600),
        Text_size = 45,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Quit",
        Action = Game.QUIT,
    )

    texts_for_menu = [Start_Game_Text, Help_Text, credits_Text ,quit_Text]
    Menu = True
    while Menu == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        MenuScreen.fill(DARK_PURPLE)
        display_regular_text("Tic-Tac-Toe", 45, 400, 50, LIGHT_BLUE,DARK_PURPLE)
    

        for texts in texts_for_menu:
            Menu_Action = texts.update(pygame.mouse.get_pos(), mouse_over_text)
            if Menu_Action is not None:
                return Menu_Action
            texts.Place_Text(MenuScreen)

        pygame.display.flip()

"""When you hit start game goes to next screen"""
def start_menu(Menu_Screen):
    menu_return = True
    return_back_to_screen = Recative_Text(
        Text_Center = (190, 670),
        Text_size = 25, 
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Return to main menu",
        Action = Game.Main_Menu,
    )
    Two_player_text = Recative_Text(
        Text_Center = (400, 300),
        Text_size = 50,
        Bg_rgb = DARK_PURPLE, 
        Text_color = LIGHT_BLUE, 
        text = "Two Player",
        Action = Game.Two_Player_mode
    )

    Vs_Ai_text = Recative_Text(
        Text_Center = (400, 500),
        Text_size = 50,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Ai",
        Action = Game.Ai_mode
    )

    texts = [Two_player_text, Vs_Ai_text, return_back_to_screen]
    while menu_return == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How do you want to play?", 40, 400, 50, LIGHT_BLUE, DARK_PURPLE)
        
        for every_text in texts:
            second_screen = every_text.update(pygame.mouse.get_pos(), mouse_over_text)
            if second_screen is not None:
                return second_screen
            every_text.Place_Text(Menu_Screen)
            
        pygame.display.flip()
    



def Help_section(Menu_Screen):
    How_to_play_3By3 = Recative_Text(
        Text_Center = (400, 300),
        Text_size = 50,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "3 By 3 Board",
        Action = Game.How_to_play_3by3
    )
    How_to_play_5By5_or_More = Recative_Text(
    Text_Center = (400, 500),
    Text_size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board or Higher",
    Action = Game.How_to_play_5by5_or_more
    )
    return_back_to_screen = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,

    )

    Text_for_help_section = [How_to_play_3By3,  How_to_play_5By5_or_More, return_back_to_screen]
    Help_section_display = True
    while Help_section_display == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How to play?", 40, 400, 50, LIGHT_BLUE, DARK_PURPLE )


        for Every_text in Text_for_help_section:
            Help_section_screen = Every_text.update(pygame.mouse.get_pos(), mouse_over_text)
            if Help_section_screen is not None:
                return Help_section_screen
            Every_text.Place_Text(Menu_Screen)

        pygame.display.flip()



def HowToPlay3X3Board(Menu_Screen):
    return_back_to_screen = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to help screen",
    Action = Game.Help_screen
    )
    return_back_to_help_screen = Recative_Text(
    Text_Center = (615, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu
)

    return_back = [return_back_to_screen, return_back_to_help_screen]
    display_Text = True
    while display_Text == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How to play 3 by 3 board", 30, 400, 50, LIGHT_BLUE, DARK_PURPLE)
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

        for texts in return_back:
            go_back = texts.update(pygame.mouse.get_pos(), mouse_over_text)
            if go_back is not None:
                return go_back
            texts.Place_Text(Menu_Screen)

        pygame.display.flip()


def HowToPlay5X5BoardOrHigher(Menu_Screen):
    return_back_to_screen = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Help_screen
    )

    return_back = [return_back_to_screen]
    display_Text = True
    while display_Text == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("How to play 5 by 5 board or higher", 30, 400, 50, LIGHT_BLUE, DARK_PURPLE)
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



        for text in return_back:
            go_back_to_help_section = text.update(pygame.mouse.get_pos(), mouse_over_text)
            if go_back_to_help_section is not None:
                return go_back_to_help_section
            text.Place_Text(Menu_Screen)

        
        pygame.display.flip()



def credits_section(Menu_Screen):
    return_back_to_screen = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )
    text_to_return = [return_back_to_screen]
    credits_Display = True
    while credits_Display == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Credits", 50, 400, 300, LIGHT_BLUE, DARK_PURPLE)
        display_regular_text("Made by Tennessee Foster", 45, 400, 350, LIGHT_BLUE, DARK_PURPLE)

        for text in text_to_return:
            return_back = return_back_to_screen.update(pygame.mouse.get_pos(), mouse_over_text)
            if return_back is not None:
                return return_back
            text.Place_Text(Menu_Screen)

        pygame.display.flip()


"""Two Player Mode """
def Two_Player_Mode(Menu_Screen):
    Board_size_3X3 = Recative_Text(
    Text_Center = (400, 200),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "3 By 3 Board",
    Action = None
    )
    Board_size_5X5 = Recative_Text(
    Text_Center = (400, 280),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board",
    Action = None
    )
    Board_size_7X7 = Recative_Text(
    Text_Center = (400, 360),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "7 By 7 Board",
    Action = None
    )
    Board_size_10X10 = Recative_Text(
    Text_Center = (400, 440),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "10 By 10 Board",
    Action = None
    )
    Board_size_20X20 = Recative_Text(
    Text_Center = (400, 520),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "20 By 20 Board",
    Action = None
    )

    Board_size_30X30 = Recative_Text(
    Text_Center = (400, 600),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "30 By 30 Board",
    Action = None
    )

    return_back_to_game_mode = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to game menu",
    Action = Game.Start_game_next_screen,
    )
    return_back_to_screen = Recative_Text(
    Text_Center = (615, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )

    board_sizes = [Board_size_3X3,Board_size_5X5, Board_size_7X7,
    Board_size_10X10, Board_size_20X20, Board_size_30X30, return_back_to_game_mode, return_back_to_screen ]
    choose_board_size = True

    while choose_board_size == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Choose Your Board", 40, 400, 50, LIGHT_BLUE,DARK_PURPLE)

        for Every_board_size in board_sizes:
            Boards = Every_board_size.update(pygame.mouse.get_pos(), mouse_over_text)
            if Boards is not None:
                return Boards
            Every_board_size.Place_Text(Menu_Screen)

        pygame.display.flip()


def Ai_Mode(Menu_Screen):
    Board_size_3X3 = Recative_Text(
        Text_Center = (400, 200),
        Text_size = 35, 
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "3 By 3 Board",
        Action = None
    )
    Board_size_5X5 = Recative_Text(
    Text_Center = (400, 280),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "5 By 5 Board",
    Action = None
    )
    Board_size_7X7 = Recative_Text(
    Text_Center = (400, 360),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "7 By 7 Board",
    Action = None
    )
    Board_size_10X10 = Recative_Text(
    Text_Center = (400, 440),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "10 By 10 Board",
    Action = None
    )
    Board_size_20X20 = Recative_Text(
    Text_Center = (400, 520),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "20 By 20 Board",
    Action = None
    )

    Board_size_30X30 = Recative_Text(
    Text_Center = (400, 600),
    Text_size = 35, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "30 By 30 Board",
    Action = None
    )

    return_back_to_screen_game_mode = Recative_Text(
    Text_Center = (190, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to game mode",
    Action = Game.Start_game_next_screen,
    )
    return_back_to_screen = Recative_Text(
    Text_Center = (615, 670),
    Text_size = 25, 
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text = "Return to main menu",
    Action = Game.Main_Menu,
    )

    board_sizes = [Board_size_3X3,Board_size_5X5, Board_size_7X7,
    Board_size_10X10, Board_size_20X20, Board_size_30X30, return_back_to_screen_game_mode, return_back_to_screen ]
    choose_board_size = True

    while choose_board_size == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
        Menu_Screen.fill(DARK_PURPLE)
        display_regular_text("Choose Your Board", 40, 400, 50, LIGHT_BLUE,DARK_PURPLE)

        for Every_board_size in board_sizes:
            Boards = Every_board_size.update(pygame.mouse.get_pos(), mouse_over_text)
            if Boards is not None:
                return Boards
            Every_board_size.Place_Text(Menu_Screen)

        pygame.display.flip()



menu_loop()