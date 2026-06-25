import pygame
import sys

from src.CONST import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from src.Level import Level
from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.fase_atual = Menu(self.window)

    def run(self):
        while True:
            dt = self.clock.tick(60)

            # Só processa eventos quando NÃO está no Menu
            # (o Menu tem seu próprio loop de eventos interno)
            if not isinstance(self.fase_atual, Menu):
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            result = self.fase_atual.run(dt)

            if result == MENU_OPTION[0]:
                self.fase_atual = Level(self.window, "Level_1", result)

            elif result == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()