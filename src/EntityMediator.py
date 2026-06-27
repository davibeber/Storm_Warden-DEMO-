import pygame
from src.CONST import WIN_WIDTH
from src.Enemy import Enemy


class EntityMediator:
    def __init__(self):
        self.player = None
        self.enemy_list: list[Enemy] = []

        # --- Configurações da Horda ---
        self.max_enemies = 10
        self.enemies_spawned = 0
        self.spawn_cooldown = 3000
        self.last_spawn_time = pygame.time.get_ticks()

    def register_player(self, player):
        self.player = player

    def spawn_enemy_outside_screen(self, camera_x):
        if self.enemies_spawned < self.max_enemies:
            pos_x_fora_da_tela = camera_x + WIN_WIDTH + 50
            pos_y_chao = 170
            novo_orc = Enemy("Orc_Warrior", (pos_x_fora_da_tela, pos_y_chao))
            novo_orc.speed = 70
            self.enemy_list.append(novo_orc)
            self.enemies_spawned += 1

    def update(self, dt, camera_x):
        if not self.player:
            return

        # Spawn com cooldown
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.last_spawn_time > self.spawn_cooldown:
            self.spawn_enemy_outside_screen(camera_x)
            self.last_spawn_time = tempo_atual

        # Posição real do player no mundo (tela + offset da câmera)
        player_real_x = self.player.rect.x + camera_x

        # Rect do player em coordenadas de mundo para colisão correta
        player_world_rect = self.player.rect.move(camera_x, 0)

        for enemy in self.enemy_list[:]:
            # 1. IA e movimentação
            enemy.move(dt, player_real_x)

            # 2. Player ataca Orc
            if (
                self.player.state == "attack"
                and self.player.atacando_no_frame
                and not self.player.ja_causou_dano
                and player_world_rect.colliderect(enemy.rect)
            ):
                enemy.take_damage(self.player.dano)
                self.player.ja_causou_dano = True

            # 3. Orc ataca Player
            #    Se o player estiver defendendo (Q), o golpe é bloqueado sem causar dano
            if (
                enemy.state == "orc_attack_1"
                and enemy.esta_no_frame_de_ataque()
                and not enemy.ja_causou_dano
                and enemy.rect.colliderect(player_world_rect)
            ):
                if self.player.state != "defend":
                    self.player.take_damage(10)
                enemy.ja_causou_dano = True  # orc não repete o hit mesmo se bloqueado

            # 4. Remove orcs mortos após animação terminar
            if enemy.state == "orc_dead" and enemy.is_animation_finished():
                self.enemy_list.remove(enemy)