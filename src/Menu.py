import pygame
from pygame import Surface, Rect
from pygame.font import Font
from src.CONST import MENU_OPTION, COLOR_WHITE, COLOR_YELLOW, WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window

        # Carregamento separado para evitar sobreposição
        self.bg_surf = pygame.image.load("./assets/backgrounds/orig_lightning.png").convert_alpha()
        self.logo_surf = pygame.image.load("./assets/GUI/logo.png").convert_alpha()

        # Definição dos retângulos de posicionamento
        self.bg_rect = self.bg_surf.get_rect(topleft=(0, 0))
        self.logo_rect = self.logo_surf.get_rect(center=(WIN_WIDTH // 2, 80))

        pygame.mixer_music.load("./assets/soundtrack/oliver siimon - epic cinematic background music 2 a major 85.mp3")
        pygame.mixer_music.play(-1)

        self.menu_option = 0

    def run(self, dt, events):
        # 1. Renderização de cenário
        self.window.blit(self.bg_surf, self.bg_rect)
        self.window.blit(self.logo_surf, self.logo_rect)

        # 2. Lógica de Título e Opções
        self.menu_text(60, "Storm Warden", (255, 174, 0), (WIN_WIDTH // 2, 70))

        mouse_pos = pygame.mouse.get_pos()
        rects_das_opcoes = []

        for i, option in enumerate(MENU_OPTION):
            posicao_centro = (WIN_WIDTH // 2, 180 + 50 * i)
            cor = COLOR_YELLOW if i == self.menu_option else COLOR_WHITE

            opcao_rect = self.menu_text(28, option, cor, posicao_centro)
            rects_das_opcoes.append(opcao_rect)

            if opcao_rect.collidepoint(mouse_pos):
                self.menu_option = i

        # 3. Processamento de eventos
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.menu_option = (self.menu_option + 1) % len(MENU_OPTION)
                elif event.key == pygame.K_UP:
                    self.menu_option = (self.menu_option - 1) % len(MENU_OPTION)
                elif event.key == pygame.K_RETURN:
                    return MENU_OPTION[self.menu_option]

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for i, opcao_rect in enumerate(rects_das_opcoes):
                    if opcao_rect.collidepoint(mouse_pos):
                        return MENU_OPTION[i]

        return None

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple) -> Rect:
        text_font: Font = pygame.font.Font(None, text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
        return text_rect