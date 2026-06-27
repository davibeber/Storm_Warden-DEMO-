import pygame
from src.EntityFactory import EntityFactory

class Player:
    def __init__(self, window, name: str):
        self.window = window
        self.name = name
        self.Player_list: list = []

        self.animacoes = {
            "idle": EntityFactory.get_entity("idle"),
            "run": EntityFactory.get_entity("run"),
            "jump": EntityFactory.get_entity("jump"),
            "defend": EntityFactory.get_entity("defend"),
            "attack": EntityFactory.get_entity("attack_1"),
            "hurt": EntityFactory.get_entity("hurt"),
            "dead": EntityFactory.get_entity("dead"),
        }

        self.state = "idle"
        self.Player_list = self.animacoes[self.state]

        if self.Player_list:
            self.rect = self.Player_list[0].rect.copy()
        else:
            self.rect = pygame.Rect(200, 146, 128, 128)

        self.rect.x = 100
        self.frame_index = 0
        self.animation_timer = 0
        self.frame_delay = 200

        self.velocidade_y = 0
        self.gravidade = 0.6
        self.forca_pulo = -10.5
        self.no_chao = True
        self.olhando_esquerda = False

        # --- ATRIBUTOS DE COMBATE E HUD ---
        self.hp_max = 100
        self.hp_atual = 100
        self.dano = 25
        self.atacando_no_frame = False   # True apenas nos frames de hit do ataque
        self.ja_causou_dano = False       # Garante hit único por swing
        self.largura_barra_max = 150

        # Cooldown de dano recebido (evita levar dano a cada frame)
        self.invencivel = False
        self.invencivel_timer = 0
        self.invencivel_duracao = 800     # ms de invencibilidade após tomar dano

        self.morto = False

    # ------------------------------------------------------------------
    # COMBATE
    # ------------------------------------------------------------------
    def take_damage(self, dano):
        if self.invencivel or self.morto:
            return
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.hp_atual = 0
            self.morto = True
            self._set_state("dead")
        else:
            self._set_state("hurt")
            self.invencivel = True
            self.invencivel_timer = 0

    def _set_state(self, novo_estado):
        if self.state != novo_estado:
            self.state = novo_estado
            self.Player_list = self.animacoes[self.state]
            self.frame_index = 0
            self.animation_timer = 0

    # ------------------------------------------------------------------
    # UPDATE (animação + timers)
    # ------------------------------------------------------------------
    def update(self, dt):
        # Invencibilidade pós-dano
        if self.invencivel:
            self.invencivel_timer += dt
            if self.invencivel_timer >= self.invencivel_duracao:
                self.invencivel = False
                self.invencivel_timer = 0

        self.animation_timer += dt

        # Delay por estado
        if self.state == "attack":
            delay_atual = 100
            # Frames 2 e 3 são os frames de impacto
            self.atacando_no_frame = (self.frame_index in [2, 3])
        elif self.state in ("hurt", "dead"):
            delay_atual = 120
            self.atacando_no_frame = False
        else:
            delay_atual = 140 if not self.no_chao else self.frame_delay
            self.atacando_no_frame = False

        if self.animation_timer >= delay_atual:
            self.animation_timer = 0
            ultimo_frame = self.frame_index == len(self.Player_list) - 1

            if self.state == "attack" and ultimo_frame:
                # Ataque terminou → volta ao idle
                self._set_state("idle")
                self.atacando_no_frame = False
                self.ja_causou_dano = False

            elif self.state == "hurt" and ultimo_frame:
                # Hurt terminou → volta ao idle
                _set_state = self._set_state  # alias
                _set_state("idle")

            elif self.state == "dead":
                # Congela no último frame
                if not ultimo_frame:
                    self.frame_index += 1
            else:
                self.frame_index = (self.frame_index + 1) % len(self.Player_list)

    # ------------------------------------------------------------------
    # HUD
    # ------------------------------------------------------------------
    def desenhar_hud(self):
        proporcao = self.hp_atual / self.hp_max
        largura_verde = int(self.largura_barra_max * proporcao)
        pos_x, pos_y = 15, 15

        pygame.draw.rect(self.window, (100, 0, 0), (pos_x, pos_y, self.largura_barra_max, 12))
        pygame.draw.rect(self.window, (34, 177, 76), (pos_x, pos_y, largura_verde, 12))
        pygame.draw.rect(self.window, (0, 0, 0), (pos_x - 1, pos_y - 1, self.largura_barra_max + 2, 14), 1)

    # ------------------------------------------------------------------
    # MOVIMENTO
    # ------------------------------------------------------------------
    def move(self):
        if self.morto:
            return

        mouse_pressed = pygame.mouse.get_pressed()
        pressed_key = pygame.key.get_pressed()
        proximo_estado = "idle"

        # Gravidade
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y

        if self.rect.y >= 146:
            self.rect.y = 146
            self.velocidade_y = 0
            self.no_chao = True
        else:
            self.no_chao = False

        # Não interrompe animações de ataque, hurt ou morte
        if self.state in ("attack", "hurt", "dead"):
            return

        if mouse_pressed[0] and self.no_chao:
            proximo_estado = "attack"
            self.ja_causou_dano = False       # reseta flag a cada novo ataque
        elif pressed_key[pygame.K_q] and self.no_chao:
            proximo_estado = "defend"
        elif pressed_key[pygame.K_a] and self.rect.x > 0:
            self.rect.centerx -= 2
            if self.no_chao:
                proximo_estado = "run"
            self.olhando_esquerda = True
        elif pressed_key[pygame.K_d] and self.rect.x < 550:
            self.rect.centerx += 2
            if self.no_chao:
                proximo_estado = "run"
            self.olhando_esquerda = False

        if pressed_key[pygame.K_SPACE] and self.no_chao:
            self.velocidade_y = self.forca_pulo
            self.no_chao = False

        if not self.no_chao:
            proximo_estado = "jump"

        if proximo_estado != self.state:
            self._set_state(proximo_estado)

    # ------------------------------------------------------------------
    # DRAW
    # ------------------------------------------------------------------
    def draw(self):
        if self.Player_list:
            frame = self.Player_list[self.frame_index]
            # Pisca quando invencível
            if self.invencivel and (pygame.time.get_ticks() // 100) % 2 == 0:
                pass  # pula o blit para efeito de piscar
            elif self.olhando_esquerda:
                sprite_invertido = pygame.transform.flip(frame.surf, True, False)
                rect_invertido = sprite_invertido.get_rect(center=self.rect.center)
                self.window.blit(sprite_invertido, rect_invertido)
            else:
                self.window.blit(frame.surf, self.rect)
        self.desenhar_hud()