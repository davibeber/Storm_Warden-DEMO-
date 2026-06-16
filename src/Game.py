import pygame

from src.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # inicia o uso do pygame
        # Criando a "janela" para o jogo
        self.window = pygame.display.set_mode(size=(600, 480))


    def run(self):

        while True:
            menu=Menu(self.window)
            menu.run()
            pass


            # Check for all events / traduzir isso dps
            # for events in pygame.event.get():
                # Entender melhor isso
                # if events.type == pygame.QUIT:
                #   pygame.quit()  # Close Window
                #    quit()  # end pygame