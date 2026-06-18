import pygame

from src.CONST import MENU_OPTION
from src.Level import Level
from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # inicia o uso do pygame
        # Criando a "janela" para o jogo
        self.window = pygame.display.set_mode(size=(576, 324))


    def run(self):
        while True: 
            menu=Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, "Level_1",menu_return)
                level_return = level.run()
                pass

            elif menu_return== MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass
