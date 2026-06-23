from pygame.examples.grid import WINDOW_WIDTH

from src.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -=1
        if self.rect.right<=0:
            self.rect.left += WINDOW_WIDTH



