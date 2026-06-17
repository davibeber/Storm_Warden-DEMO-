import pygame

from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # inicia o uso do pygame
        # Criando a "janela" para o jogo
        self.window = pygame.display.set_mode(size=(576, 324))


    def run(self):

        while True:
            menu=Menu(self.window)
            menu.run()


