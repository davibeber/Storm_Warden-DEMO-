import pygame
from src.CONST import WIN_WIDTH
from src.Enemy import Enemy
from src.Boss import Boss
from src.Potion import Potion


class EntityMediator:
    def __init__(self):
        self.player = None
        self.enemy_list: list[Enemy] = []
        self.potion_list: list[Potion] = []
        self.boss: Boss = None

        # --- Configurações da Horda ---
        self.max_enemies = 10
        self.enemies_spawned = 0
        self.spawn_cooldown = 3000
        self.last_spawn_time = pygame.time.get_ticks()

        # Contagem de orcs mortos para drops e spawn do boss
        self.orcs_mortos = 0
        self.boss_spawnado = False

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

    def spawn_boss(self, camera_x):
        pos_x = camera_x + WIN_WIDTH + 100
        self.boss = Boss((pos_x, 170))

    def update(self, dt, camera_x):
        if not self.player:
            return

        # Spawn de orcs com cooldown (apenas enquanto não atingiu o limite)
        tempo_atual = pygame.time.get_ticks()
        if (
            self.enemies_spawned < self.max_enemies
            and tempo_atual - self.last_spawn_time > self.spawn_cooldown
        ):
            self.spawn_enemy_outside_screen(camera_x)
            self.last_spawn_time = tempo_atual

        # Posição real do player no mundo
        player_real_x = self.player.rect.x + camera_x
        player_world_rect = self.player.rect.move(camera_x, 0)

        # ------------------------------------------------------------------
        # ORCS
        # ------------------------------------------------------------------
        for enemy in self.enemy_list[:]:
            enemy.move(dt, player_real_x)

            # Player ataca orc
            if (
                self.player.state == "attack"
                and self.player.atacando_no_frame
                and not self.player.ja_causou_dano
                and player_world_rect.colliderect(enemy.rect)
            ):
                enemy.take_damage(self.player.dano)
                self.player.ja_causou_dano = True

            # Orc ataca player
            if (
                enemy.state == "orc_attack_1"
                and enemy.esta_no_frame_de_ataque()
                and not enemy.ja_causou_dano
                and enemy.rect.colliderect(player_world_rect)
            ):
                if self.player.state != "defend":
                    self.player.take_damage(10)
                enemy.ja_causou_dano = True

            # Remove orc morto e aplica drops / lógica de boss
            if enemy.state == "orc_dead" and enemy.is_animation_finished():
                self.enemy_list.remove(enemy)
                self.orcs_mortos += 1

                # Poção a cada 2 mortes (mortes 2, 4, 6, 8, 10)
                if self.orcs_mortos % 2 == 0:
                    drop_pos = (enemy.rect.x, enemy.rect.y + 20)
                    self.potion_list.append(Potion(drop_pos))

                # O Boss aparece após todos os 10 orcs serem eliminados
                if self.orcs_mortos >= self.max_enemies and not self.boss_spawnado:
                    self.spawn_boss(camera_x)
                    self.boss_spawnado = True

        # ------------------------------------------------------------------
        # BOSS
        # ------------------------------------------------------------------
        if self.boss:
            self.boss.move(dt, player_real_x)

            # Player ataca boss
            if (
                self.player.state == "attack"
                and self.player.atacando_no_frame
                and not self.player.ja_causou_dano
                and player_world_rect.colliderect(self.boss.rect)
            ):
                self.boss.take_damage(self.player.dano)
                self.player.ja_causou_dano = True

            # Boss ataca o jogador
            if (
                self.boss.state == "B_attack"
                and self.boss.esta_no_frame_de_ataque()
                and not self.boss.ja_causou_dano
                and self.boss.rect.colliderect(player_world_rect)
            ):
                if self.player.state != "defend":
                    self.player.take_damage(self.boss.dano)
                self.boss.ja_causou_dano = True

            # Remove boss após animação de morte terminar
            if self.boss.state == "B_dead" and self.boss.is_animation_finished():
                self.boss = None

        # ------------------------------------------------------------------
        # POÇÕES
        # ------------------------------------------------------------------
        for potion in self.potion_list[:]:
            if player_world_rect.colliderect(potion.rect):
                cura = min(Potion.CURA, self.player.hp_max - self.player.hp_atual)
                self.player.hp_atual += cura
                self.potion_list.remove(potion)