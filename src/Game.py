import pygame
import sys

from src.CONST import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT
from src.Level import Level
from src.Menu import Menu
from src.Instructions import Instructions
from src.GameOver import GameOver
from src.WinScreen import WinScreen


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

            if result == MENU_OPTION[0]:        # Jogar
                self.fase_atual = Level(self.window, "Level_1", result)

            elif result == MENU_OPTION[1]:      # Comandos e Missão
                self.fase_atual = Instructions(self.window)

            elif result == MENU_OPTION[2]:      # Sair
                pygame.quit()
                sys.exit()

            elif result == "MENU":              # Voltar ao menu principal
                self.fase_atual = Menu(self.window)

            elif result == "GAME_OVER":         # Jogador morreu
                self.fase_atual = GameOver(self.window)

            elif result == "RESTART":           # Recomeçar do Level 1
                self.fase_atual = Level(self.window, "Level_1", MENU_OPTION[0])

            elif result == "WIN":               # Boss foi derrotado
                self.fase_atual = WinScreen(self.window)

            pygame.display.flip()