import pygame
import sys

from src.CONST import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from src.Level import Level
from src.Menu import Menu
from src.Instructions import Instructions  # Descomentado!

class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode(
            size=(WIN_WIDTH, WIN_HEIGHT),
            flags=pygame.FULLSCREEN | pygame.SCALED
        )

        self.clock = pygame.time.Clock()
        self.fase_atual = Menu(self.window)

    def run(self):
        while True:
            dt = self.clock.tick(60)
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            result = self.fase_atual.run(dt, events)

            # --- LÓGICA DE TRANSIÇÃO DE TELAS ---

            if result == MENU_OPTION[0]:  # "Jogar"
                self.fase_atual = Level(self.window, "Level_1", result)

            elif result == MENU_OPTION[1]:  # "Como jogar"
                self.fase_atual = Instructions(self.window) # Classe instanciada!

            elif result == MENU_OPTION[2]:  # "Sair"
                pygame.quit()
                sys.exit()

            elif result == "MENU":  # Voltar ao menu principal
                self.fase_atual = Menu(self.window)

            pygame.display.flip()