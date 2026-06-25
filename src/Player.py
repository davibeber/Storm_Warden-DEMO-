import pygame

class Player:
    def __init__(self, window, name: str):
        self.window = window
        self.name = name
        self.Player_list: list = []

        from src.EntityFactory import EntityFactory
        self.Player_list.extend(EntityFactory.get_entity("idle"))  # ✅ minúsculo

        if self.Player_list:
            self.rect = self.Player_list[0].rect.copy()
        else:
            self.rect = pygame.Rect(200, 150, 44 * 3, 65 * 3)

        # --- lógica de animação ---
        self.frame_index = 1
        self.animation_timer = 0
        self.frame_delay = 150  # ms entre frames (ajuste para acelerar/desacelerar)

    def update(self, dt):
        """dt = milliseconds desde o último frame (retorno do clock.tick)"""
        self.animation_timer += dt
        if self.animation_timer >= self.frame_delay:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.Player_list)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]    and self.rect.y > 60:
            self.rect.centery -= 1
        if pressed_key[pygame.K_DOWN]  and self.rect.y < 146:
            self.rect.centery += 1
        if pressed_key[pygame.K_LEFT]  and self.rect.x > 1:
            self.rect.centerx -= 1
        if pressed_key[pygame.K_RIGHT] and self.rect.x < 450:
            self.rect.centerx += 1

    def draw(self):
        """Desenha apenas o frame atual"""
        frame = self.Player_list[self.frame_index]
        self.window.blit(source=frame.surf, dest=self.rect)