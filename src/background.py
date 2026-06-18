from src.Entity import Entity


class Background(Entity):
    def __init__(self, name, str, position: tuple):
        super().__init__(name, str, position)

    def run(self):
        pass