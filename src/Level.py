import pygame

from src.EntityFactory import EntityFactory
from src.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.player = None
        self.menu_option = menu_option
        self.window = window
        self.name = name
        self.entity_list: list = []

        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        self.entity_list.extend(EntityFactory.get_entity("Level1Pfr"))

        self.player = Player(self.window, "Teste")
        # ❌ NÃO adicione Player_list em entity_list — o player se desenha sozinho

    def run(self, dt):  # recebe dt para repassar ao player
        # Desenha background e plataforma
        for ent in self.entity_list:
            self.window.blit(source=ent.surf, dest=ent.rect)

        # Atualiza e desenha o player
        self.player.update(dt)
        self.player.move()
        self.player.draw()


        pygame.display.flip()