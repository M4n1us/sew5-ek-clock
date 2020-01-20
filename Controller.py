import pygame
from pygame.locals import *

from AnalogUhr import AnalogUhr
from DigitalUhr import DigitalUhr


class App:
    """
    Clock that allows switching between views via A(nalog) and D(igital)
    the P button allows for switching between a continuous and jumping second hand
    """
    def __init__(self):
        """
        Initializing state methods
        """
        self._running = True
        self._display_surf = None
        self.strategy = None
        self.analog_modus = True

    def on_init(self):
        """
        Inits the game state
        :return: None
        """
        pygame.init()
        self.strategy = DigitalUhr()
        self._running = True

    def on_event(self, event):
        """
        Eventhandling for keydown of A, D, P and Quit event
        :param event: Events from pygame
        :return: None
        """
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.strategy = AnalogUhr()
            elif event.key == pygame.K_d:
                self.strategy = DigitalUhr()
            elif event.key == pygame.K_p:
                self.analog_modus = not self.analog_modus

    def on_render(self):
        """
        Renders the strategy for the clock render
        :return: None
        """
        self.strategy.render(params={"continuous": self.analog_modus})

    def on_cleanup(self):
        """
        Inits shutdown of the engine
        :return: None
        """
        pygame.quit()

    def on_execute(self):
        """
        Sets up the pygame framework and contains main loop
        :return:
        """
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()