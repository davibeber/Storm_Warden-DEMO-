import os
# Força a qualidade de escala mais próxima (Pixel Perfect / Modo Paint)
os.environ['SDL_RENDER_SCALE_QUALITY'] = 'nearest'
# Força o Pygame a usar renderização por software, evitando filtros da placa de vídeo
os.environ['SDL_VIDEODRIVER'] = 'windib'

import pygame
from src.Game import Game

if __name__ == "__main__":
    game = Game()
    game.run()