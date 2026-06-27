import pygame
from src.Entity import Entity
from src.EntityFactory import EntityFactory


class Enemy(Entity):
    def __init__(self, name, position):
        self.state = "orc_idle"
        self.direction = -1
        self.index_animacao = 0.0
        self.animation_list = EntityFactory.get_entity(self.state)

        self.speed = 80              # px/s de movimento no mundo
        self.velocidade = 0.10       # frames por tick da animação (0.05=lento, 0.20=rápido)

        self.hp_max = 50
        self.hp_atual = 50
        self.animation_finished = False

        self.frame_de_dano = 2
        self.ja_causou_dano = False

        # Invencibilidade após tomar dano (evita hit duplo por swing)
        self.invencivel = False
        self.invencivel_timer = 0
        self.invencivel_duracao = 600  # ms

        super().__init__("./assets/mobs/orc_warrior/orc_idle.png", position)

        self.rect.topleft = position
        self.pos_x = float(position[0])

    # ------------------------------------------------------------------
    # SURF
    # ------------------------------------------------------------------
    @property
    def surf(self):
        if not self.animation_list:
            return None
        index = min(int(self.index_animacao), len(self.animation_list) - 1)
        frame = self.animation_list[index]
        if self.direction == -1:
            return pygame.transform.flip(frame.surf, True, False)
        return frame.surf

    @surf.setter
    def surf(self, value):
        pass

    # ------------------------------------------------------------------
    # ESTADO
    # ------------------------------------------------------------------
    def set_state(self, new_state, speed=0.10):
        if self.state != new_state:
            self.state = new_state
            self.animation_list = EntityFactory.get_entity(self.state)
            self.index_animacao = 0.10
            self.velocidade = speed
            self.animation_finished = False
            self.ja_causou_dano = False

    # ------------------------------------------------------------------
    # COMBATE
    # ------------------------------------------------------------------
    def take_damage(self, dano):
        if self.state == "orc_dead" or self.invencivel:
            return
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.hp_atual = 0
            self.invencivel = False
            self.set_state("orc_dead", speed=0.07)
        else:
            self.set_state("orc_hurt", speed=0.08)  # lento = animação dura mais
            self.invencivel = True
            self.invencivel_timer = 0

    def is_animation_finished(self):
        return self.animation_finished

    def esta_no_frame_de_ataque(self):
        if self.state != "orc_attack_1":
            return False
        return int(self.index_animacao) >= self.frame_de_dano

    # ------------------------------------------------------------------
    # MOVIMENTO / IA
    # ------------------------------------------------------------------
    def move(self, dt, player_real_x):
        dt_s = dt / 1000.0

        # --- Timer de invencibilidade ---
        if self.invencivel:
            self.invencivel_timer += dt
            if self.invencivel_timer >= self.invencivel_duracao:
                self.invencivel = False
                self.invencivel_timer = 0

        # --- Morte ---
        if self.state == "orc_dead":
            self.index_animacao += self.velocidade
            if self.index_animacao >= len(self.animation_list):
                self.index_animacao = len(self.animation_list) - 1
                self.animation_finished = True
            return

        # --- Hurt ---
        if self.state == "orc_hurt":
            self.index_animacao += self.velocidade
            if self.index_animacao >= len(self.animation_list):
                self.set_state("orc_walk")
            return

        # --- Perseguição ---
        distancia = player_real_x - self.rect.centerx

        # Direção só atualiza fora do ataque (evita flip durante o ciclo)
        if self.state != "orc_attack_1":
            self.direction = 1 if distancia > 0 else -1

        if abs(distancia) > 55:
            # Deixa o ciclo de ataque terminar antes de voltar a andar
            if self.state == "orc_attack_1":
                self.index_animacao += self.velocidade
                if self.index_animacao >= len(self.animation_list):
                    self.index_animacao = 0.0
                    self.set_state("orc_walk")
                return

            self.set_state("orc_walk")
            self.pos_x += self.speed * self.direction * dt_s
            self.rect.x = int(self.pos_x)

        else:
            self.set_state("orc_attack_1", speed=0.10)

        # --- Avança animação ---
        self.index_animacao += self.velocidade
        if self.index_animacao >= len(self.animation_list):
            self.index_animacao = 0.0
            if self.state == "orc_attack_1":
                self.ja_causou_dano = False