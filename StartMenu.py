import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum


DARK_PURPLE = (102, 0, 102)
LIGHT_BLUE = (0, 255, 255)
pygame.display.set_caption("Tic-Tac-Toe Menu")

def Make_a_place_on_screen_for_text(text, Text_size, Text_Color, Bg_rgb):
    """ display's text on screen"""
    font = pygame.freetype.SysFont("Verdana", Text_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=Text_Color, bgcolor=Bg_rgb)
    return surface.convert_alpha()


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
        # for quit text 
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
    TITLE = 0
    NEWGAME = 1


# the main loop
def menu_loop():

    pygame.init()

    Menu_Screen = pygame.display.set_mode((800, 700))
    Game_State = Game.TITLE

    Start_menu = True
    while Start_menu == True:
        if Game_State == Game.TITLE:
            Game_State = Title_screen(Menu_Screen)
        
        if Game_State == Game.NEWGAME:
            Game_State = start_menu(Menu_Screen)
        
        if Game_State == Game.QUIT:
            pygame.quit()
            return


"""Text for menu screen"""
def Title_screen(Menu_Screen):
    Start_Game_Text = Recative_Text(
    Text_Center = (400, 300),
    Text_size = 45,
    Bg_rgb = DARK_PURPLE,
    Text_color = LIGHT_BLUE,
    text ="Start Game",
    Action = Game.NEWGAME, 
    )
    Help_Text = Recative_Text(
        Text_Center = (400, 400),
        Text_size = 45,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Help",
    )
    credits_Text = Recative_Text(
        Text_Center = (400, 500),
        Text_size = 45,
        Bg_rgb = DARK_PURPLE,
        Text_color = LIGHT_BLUE,
        text = "Credits",
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
        Menu_Screen.fill(DARK_PURPLE)
        
        for texts in texts_for_menu:
            quit_action = texts.update(pygame.mouse.get_pos(), mouse_over_text)
            if quit_action is not None:
                return quit_action
            texts.Place_Text(Menu_Screen)

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
        Action = Game.TITLE,
    )
    while menu_return == True:
        mouse_over_text = False
        for window in pygame.event.get():
            if window.type == pygame.MOUSEBUTTONUP and window.button == 1:
                mouse_over_text = True
            Menu_Screen.fill(DARK_PURPLE)  
            
            return_action = return_back_to_screen.update(pygame.mouse.get_pos(), mouse_over_text)
            if return_action is not None:
                return return_action
            return_back_to_screen.Place_Text(Menu_Screen)
            
            pygame.display.flip()



menu_loop()