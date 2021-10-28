import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect

DARK_PURPLE = (102, 0, 102)
LIGHT_BLUE = (0, 255, 255)


def Make_a_place_on_screen_for_text(text, Text_size, Text_Color, Bg_rgb):
    """ Returns surface with text on screen"""
    font = pygame.freetype.SysFont("Courier", Text_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=Text_Color, bgcolor=Bg_rgb)
    return surface.convert_alpha()


class Recative_Text(Sprite):
    """Makes the text be able to react depending on user mouse"""
    def __init__(self, Text_Center, text, Text_size, Bg_rgb, Text_color):
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

        # calls the init method of the parent sprite class
        super().__init__()

    #  is the mouse over text if yes does reactive if no goes to regular text
    @property
    def default(self):
        return self.High_lights_text[1] if self.mouse_over else self.High_lights_text[0]

    @property
    def TextReactive(self):
        return self.Reactive[1] if self.mouse_over else self.Reactive[0]

    def update(self, mouse_pos):
        if self.TextReactive.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def Place_Text(self, surface):
        """ Places the text onto menu """
        surface.blit(self.default, self.TextReactive)


pygame.init()
Menu_text = pygame.display.set_mode((800, 600))
# creates a UI Text 
Text_for_menu = Recative_Text(
    Text_Center=(400, 400),
    Text_size=30,
    Bg_rgb=DARK_PURPLE,
    Text_color=LIGHT_BLUE,
    text="Hello World",
)
# main loop
while True:
    for widnow in pygame.event.get():
        pass
    Menu_text.fill(DARK_PURPLE)
    Text_for_menu.update(pygame.mouse.get_pos())
    Text_for_menu.Place_Text(Menu_text)
    pygame.display.flip()