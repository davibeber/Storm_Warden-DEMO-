import pygame
from src.EntityFactory import EntityFactory
from src.Player import Player
from src.EntityMediator import EntityMediator
from src.CONST import WIN_WIDTH, WIN_HEIGHT, BG


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.pausado = False

        pygame.mixer_music.stop()
        pygame.mixer_music.load("./assets/soundtrack/Level_1 - jungle intense suspense horror 200.mp3")
        pygame.mixer_music.play(-1)

        btn_menu_size = (120, 35)
        gap = 80

        self.btn_pause_normal = pygame.transform.smoothscale(EntityFactory.get_entity("Pause_BTN.png").surf, (40, 40))
        self.btn_resume = pygame.transform.smoothscale(EntityFactory.get_entity("resume").surf, btn_menu_size)
        self.btn_menu = pygame.transform.smoothscale(EntityFactory.get_entity("menu").surf, btn_menu_size)
        self.btn_quit = pygame.transform.smoothscale(EntityFactory.get_entity("quit").surf, btn_menu_size)

        font = pygame.font.SysFont("Arial", 20, bold=True)
        text_surf = font.render("MENU", True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(btn_menu_size[0] // 2, btn_menu_size[1] // 2))
        self.btn_menu.blit(text_surf, text_rect)

        self.pause_btn_rect = self.btn_pause_normal.get_rect(topright=(WIN_WIDTH - 10, 10))
        self.menu_btn_rects = {
            "resume": self.btn_resume.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 - gap)),
            "menu": self.btn_menu.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2)),
            "quit": self.btn_quit.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2 + gap))
        }

        self.background_list = EntityFactory.get_entity("Level1Bg")
        self.platform_list = EntityFactory.get_entity("Level1Pfr")
        self.player = Player(self.window, "Teste")
        self.camera_x = 0
        self.mediator = EntityMediator()
        self.mediator.register_player(self.player)
        self.camera_maxima = (len(self.platform_list) * 128) - WIN_WIDTH

        # Zona morta: player anda livre entre MARGEM_ESQUERDA e MARGEM_DIREITA
        # A câmera só se move quando ele sai dessa faixa
        self.MARGEM_ESQUERDA = 150
        self.MARGEM_DIREITA = WIN_WIDTH - 150

    def run(self, dt, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.pausado:
                    if self.menu_btn_rects["resume"].collidepoint(event.pos):
                        self.pausado = False
                    elif self.menu_btn_rects["menu"].collidepoint(event.pos):
                        return "MENU"
                    elif self.menu_btn_rects["quit"].collidepoint(event.pos):
                        pygame.quit()
                        exit()
                elif self.pause_btn_rect.collidepoint(event.pos):
                    self.pausado = True

        if not self.pausado:
            self.player.update(dt)
            self.player.move()
            self.update_camera()
            self.mediator.update(dt, self.camera_x)

        self.render_game()
        return None

    def update_camera(self):
        # Câmera avança quando player passa da borda direita da zona livre
        if self.player.rect.x > self.MARGEM_DIREITA:
            deslocamento = self.player.rect.x - self.MARGEM_DIREITA
            self.camera_x = min(self.camera_x + deslocamento, self.camera_maxima)
            self.player.rect.x = self.MARGEM_DIREITA

        # Câmera recua quando player passa da borda esquerda da zona livre
        elif self.player.rect.x < self.MARGEM_ESQUERDA and self.camera_x > 0:
            deslocamento = self.MARGEM_ESQUERDA - self.player.rect.x
            self.camera_x = max(self.camera_x - deslocamento, 0)
            self.player.rect.x = self.MARGEM_ESQUERDA

    def render_game(self):
        self.window.fill(BG)

        for bg in self.background_list:
            self.window.blit(bg.surf, (bg.rect.x - (self.camera_x * 0.15), bg.rect.y))

        for pfr in self.platform_list:
            self.window.blit(pfr.surf, (pfr.rect.x - self.camera_x, pfr.rect.y))

        for enemy in self.mediator.enemy_list:
            if enemy.surf:
                self.window.blit(enemy.surf, (enemy.rect.x - self.camera_x, enemy.rect.y))

        self.player.draw()

        if self.pausado:
            overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            overlay.fill(BG)
            overlay.set_alpha(180)
            self.window.blit(overlay, (0, 0))
            self.window.blit(self.btn_resume, self.menu_btn_rects["resume"])
            self.window.blit(self.btn_menu, self.menu_btn_rects["menu"])
            self.window.blit(self.btn_quit, self.menu_btn_rects["quit"])
        else:
            self.window.blit(self.btn_pause_normal, self.pause_btn_rect)