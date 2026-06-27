import pygame
from src.CONST import BG, WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE


class Instructions:
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load("./assets/GUI/como_jogar.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

    def run(self, dt, events):
        self.window.fill(BG)
        self.window.blit(source=self.image, dest=self.rect)
        self._draw_comandos()

        for event in events:
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return "MENU"

        return None

    def _draw_comandos(self):
        font = pygame.font.SysFont("Lucida Sans Typewriter", 14)
        comandos = [
            ("Defesa: Q", COLOR_WHITE),
            ("Andar para esquerda: A", COLOR_WHITE),
            ("Andar para direita: D", COLOR_WHITE),
            ("Pular: Espaço", COLOR_WHITE),
            ("Ataque: Botão esquerdo", COLOR_WHITE),
            (" do mouse", COLOR_WHITE),
            ("Pressione qualquer tecla", (253, 255, 0)),
            ("     para voltar", (253, 255, 0)),
        ]
        x = 65
        y_inicial = 50
        espacamento = 35

        for i, (texto, cor) in enumerate(comandos):
            y = y_inicial + i * espacamento
            surf = font.render(texto, True, cor)
            self.window.blit(surf, (x, y))