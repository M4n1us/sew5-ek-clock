import pygame
from pygame.locals import *

from AnalogUhr import AnalogUhr
from DigitalUhr import DigitalUhr


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.strategy = None
        self.analog_modus = True

    def on_init(self):
        pygame.init()
        self.strategy = DigitalUhr()
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.strategy = AnalogUhr()
                print("AnalogUhr")
            elif event.key == pygame.K_d:
                self.strategy = DigitalUhr()
                print("DigitalUhr")
            elif event.key == pygame.K_p:
                self.analog_modus = not self.analog_modus
                print("ChangedModus to: " + str(self.analog_modus))

    def on_render(self):
        self.strategy.render(params={"continuous": self.analog_modus})

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
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