import pygame as pygame
import datetime

from Strategy import Uhr


class DigitalUhr(Uhr):
    """
    Pygame Rendering for a digital clock displaying the current time as text
    """
    def __init__(self):
        """
        Inits the main window and renders first background
        """
        super().__init__()
        self.screen = pygame.display.set_mode((640, 400), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def render(self, params=None):
        """
        Main Rendering function, renders time as black text on white background with the HH:MM:SS format
        :param params: Default: None, can contain information for the renderer
        :return: none
        """
        time = datetime.datetime.now()
        font = pygame.font.Font(None, 120)
        text = font.render(time.strftime("%H:%M:%S"), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = self.background.get_rect().centerx
        textpos.centery = self.background.get_rect().centery
        self.background.fill((250, 250, 250))
        self.screen.blit(self.background, (0, 0))
        self.background.blit(text, textpos)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()