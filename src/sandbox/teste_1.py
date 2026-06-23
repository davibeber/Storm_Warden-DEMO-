import pygame
import sys
# o que é sys?
# É um módulo nativo do Python (System).

from src.CONST import MENU_OPTION
from src.Level import Level
from src.Menu import Menu


class Game: # Classe controle
    def __init__(self):
        pygame.init()  # inicia o uso do pygame
        # Criando a "janela" para o jogo
        self.window = pygame.display.set_mode(size=(576, 324))
        # Padrão tela pequena 576, 324
        # Tamanho maximo da minha tela 1920, 1080
        self.clock = pygame.time.Clock() # O que seria o Clock? relogio, ok, mas provavelmente tem relação com giro
        self.fase_atual = Menu(self.window) # O jogo começa no Menu

    def run(self):
        # Em arquitetura de jogos, o motor só pode ter UM while True principal.
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    sys.exit()

            menu_return = self.fase_atual.run()

            # menu=Menu(self.window)
            # menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                self.fase_atual = Level(self.window, "Level_1", menu_return)
                # Nós DESTRUÍMOS o Menu e colocamos o Level 1 no lugar dele!
                # isso não pode ser bom, pois está considerando apenas uma fase, precisa ser generico para aceitar
                # mais fases

                # level = Level(self.window, "Level_1",menu_return)
                # level_return = level.run()

            elif menu_return== MENU_OPTION[2]:
                pygame.quit()
                sys.exit()

            pygame.display.flip()
            self.clock.tick(60)  # Garante 60 FPS para o jogo todo (menu, Level 1, Level 2...)










            # TODO - PARA RODAR A MUSICA DO LEVEL 1
            pygame.mixer_music.load()
            pygame.mixer_music.play(-1)
            clock = pygame.time.Clock()
            # Garantir que rode num clock especifico, FPS travado na qual for escolhido

            while True:
                clock.tick(60)

                for ent in self.entity_list:
                    self.window.blit(source=ent.surf, dest=ent.rect)
                    ent.move()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()



            # TODO - PRINT DO FPS
            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()