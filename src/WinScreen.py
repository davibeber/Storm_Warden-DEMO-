import pygame
from src.CONST import BG, WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE


class WinScreen:
    # Tela exibida após derrotar o Boss

    def __init__(self, window):
        self.window = window

        header_raw = pygame.image.load("./assets/gameover/header_win.png").convert_alpha()
        btn_raw = pygame.image.load("./assets/gameover/exit_BTN.png").convert_alpha()

        header_w = int(WIN_WIDTH * 0.60)
        header_h = int(header_raw.get_height() * (header_w / header_raw.get_width()))
        btn_w = int(WIN_WIDTH * 0.22)  # menor que antes (era 0.35)
        btn_h = int(btn_raw.get_height() * (btn_w / btn_raw.get_width()))

        self.header = pygame.transform.smoothscale(header_raw, (header_w, header_h))
        self.btn_exit = pygame.transform.smoothscale(btn_raw, (btn_w, btn_h))

        self.header_rect = self.header.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - 60))
        self.btn_rect = self.btn_exit.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 85))  # mais abaixo (era +60)

        self.font = pygame.font.SysFont("Arial", 14)
        self.texto_surf = self.font.render(
            "Obrigado por jogar a Demo de Storm Warden.", True, COLOR_WHITE
        )
        self.texto_rect = self.texto_surf.get_rect(
            center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + 20)
        )

    def run(self, dt, events):
        self.window.fill(BG)
        self.window.blit(self.header, self.header_rect)
        self.window.blit(self.texto_surf, self.texto_rect)
        self.window.blit(self.btn_exit, self.btn_rect)

        mouse_pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_rect.collidepoint(mouse_pos):
                    return "MENU"

        return None