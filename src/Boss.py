import pygame
from src.Enemy import Enemy
from src.EntityFactory import EntityFactory


class Boss(Enemy):
    # Orc Berserk — boss que aparece após os 10 orcs serem derrotados.

    def __init__(self, position: tuple):
        # Inicializa o Enemy base com estado idle do boss
        super().__init__("Boss", position)

        # Sobrescreve atributos do Enemy com os do boss
        self.state = "B_idle"
        self.animation_list = EntityFactory.get_entity(self.state)
        self.index_animacao = 0.0

        self.hp_max = 200
        self.hp_atual = 200
        self.speed = 60
        self.velocidade = 0.08
        self.dano = 25            # usado pelo mediator ao aplicar dano ao player

        self.frame_de_dano = 5   # B_attack tem 36 frames; dano começa no frame 5
        self.ja_causou_dano = False
        self.animation_finished = False

        self.invencivel = False
        self.invencivel_timer = 0
        self.invencivel_duracao = 800

        self.pos_x = float(position[0])
        self.rect.topleft = position

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
    def set_state(self, new_state, speed=0.08):
        if self.state != new_state:
            self.state = new_state
            self.animation_list = EntityFactory.get_entity(self.state)
            self.index_animacao = 0.0
            self.velocidade = speed
            self.animation_finished = False
            self.ja_causou_dano = False

    # ------------------------------------------------------------------
    # COMBATE
    # ------------------------------------------------------------------
    def take_damage(self, dano):
        if self.state == "B_dead" or self.invencivel:
            return
        self.hp_atual -= dano
        if self.hp_atual <= 0:
            self.hp_atual = 0
            self.invencivel = False
            self.set_state("B_dead", speed=0.06)
        else:
            self.set_state("B_hurt", speed=0.08)
            self.invencivel = True
            self.invencivel_timer = 0

    def is_animation_finished(self):
        return self.animation_finished

    def esta_no_frame_de_ataque(self):
        if self.state != "B_attack":
            return False
        return int(self.index_animacao) >= self.frame_de_dano

    # ------------------------------------------------------------------
    # MOVIMENTO
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
        if self.state == "B_dead":
            self.index_animacao += self.velocidade
            if self.index_animacao >= len(self.animation_list):
                self.index_animacao = len(self.animation_list) - 1
                self.animation_finished = True
            return

        # --- Hurt ---
        if self.state == "B_hurt":
            self.index_animacao += self.velocidade
            if self.index_animacao >= len(self.animation_list):
                self.set_state("B_walk")
            return

        # --- Perseguição ---
        distancia = player_real_x - self.rect.centerx

        if self.state != "B_attack":
            self.direction = 1 if distancia > 0 else -1

        if abs(distancia) > 60:
            # Deixa o ciclo de ataque terminar antes de voltar a andar
            if self.state == "B_attack":
                self.index_animacao += self.velocidade
                if self.index_animacao >= len(self.animation_list):
                    self.index_animacao = 0.0
                    self.set_state("B_walk")
                return

            self.set_state("B_walk")
            self.pos_x += self.speed * self.direction * dt_s
            self.rect.x = int(self.pos_x)
        else:
            self.set_state("B_attack", speed=0.08)

        # --- Avança animação ---
        self.index_animacao += self.velocidade
        if self.index_animacao >= len(self.animation_list):
            self.index_animacao = 0.0
            if self.state == "B_attack":
                self.ja_causou_dano = False