import pygame
from src.CONST import BG, WIN_WIDTH, WIN_HEIGHT


class GameOver:
    # Tela exibida quando o jogador morre.

    def __init__(self, window):
        self.window = window

        header_raw = pygame.image.load("./assets/gameover/header_lose.png").convert_alpha()
        btn_raw = pygame.image.load("./assets/gameover/start_BTN.png").convert_alpha()

        # Redimensiona: header ocupa ~60% da largura, botão ~35%
        header_w = int(WIN_WIDTH * 0.60)
        header_h = int(header_raw.get_height() * (header_w / header_raw.get_width()))
        btn_w = int(WIN_WIDTH * 0.35)
        btn_h = int(btn_raw.get_height() * (btn_w / btn_raw.get_width()))

        self.header = pygame.transform.smoothscale(header_raw, (header_w, header_h))
        self.btn_start = pygame.transform.smoothscale(btn_raw, (btn_w, btn_h))

        self.header_rect = self.header.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
        self.btn_rect = self.btn_start.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 60))

    def run(self, dt, events):
        self.window.fill(BG)
        self.window.blit(self.header, self.header_rect)
        self.window.blit(self.btn_start, self.btn_rect)

        mouse_pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_rect.collidepoint(mouse_pos):
                    return "RESTART"

        return None