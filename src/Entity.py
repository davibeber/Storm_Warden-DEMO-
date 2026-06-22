from abc import ABC, abstractmethod
import pygame.image


class Entity(ABC): # Evita repetição de codigo
    def __init__(self, name: str,position: tuple):
        self.Player = None
        self.background = None
        self.name = name
        # Agora o 'name' já deve vir com o caminho completo e correto de onde ele estiver

        self.surf= pygame.image.load(name)
        # self.surf = pygame.image.load(name).convert_alpha()

        self.rect = self.surf.get_rect(left=position[0],top=position[1])
        self.speed = 0



    @abstractmethod
    def move(self,):
        pass