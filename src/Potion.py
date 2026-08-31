import pygame
from src.EntityFactory import EntityFactory


class Potion:
    # Poção de vida que cai no chão quando um orc morre.

    CURA = 30  # HP restaurado ao coletar

    def __init__(self, position: tuple):
        obj = EntityFactory.get_entity("vida")
        self.surf = obj.surf
        self.rect = self.surf.get_rect(topleft=position)
        self.coletada = False