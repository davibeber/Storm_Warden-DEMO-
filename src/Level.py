import sys

import pygame

from src.Entity import Entity
from src.EntityFactory import EntityFactory
from src.Player import Player


class Level:
    def __init__(self, window, name, menu_option):
        self.window=window
        self.name=name
        self.entity_list: list[Entity]=[]
        # Guarda as instancias, o python acha o que precisa na lista, "pula" e executa
        self.entity_list.extend(EntityFactory.get_entity("Level1Bg"))
        # Essa ultima linha pede a classe EntityFactory os assets para montar o level
        self.entity_list.extend(EntityFactory.get_entity("Level1Pfr"))
        self.player = Player(self.window, "Teste")
        self.entity_list.extend(self.player.Player_list)


        # Não guarda arquivos em si, apenas objetos que sabem gerenciar os arquivos.
        # Mas pq guardar os objetos? pq guardar algo assim? Se fosse dados, até faz sentido,
        # dados em lista, dicionarios, para serem manipulados e consultados, blz mas pq isso?


        # O estilo do meu jogo (game_mode) será apenas single player.
        # append(objeto) --> pega um unico objeto e poe dentro da caixa. caso tiver mais de um,
        # ele junta tudo e como se fosse um só, provavelmente isso interfere no efeito parallax

        # extend(lista) --> os assets são pegos e postos de forma isolada para alterar individualmente


    
    def run(self):


        for ent in self.entity_list:
            self.window.blit(source=ent.surf,dest=ent.rect)
            # ent.move()
            # aqui seria um:  ent.move() = velocidade_jogador ?

        pygame.display.flip()
        # Comando responsável por atualizar a tela do jogo para mostrar as últimas mudanças feitas.
        # Faz um pré-carregamento para dps atualizar a tela.
        # Sem isso, a tela estaria piscando, o efeito "flickering", pois está atualizando em tempo real
        # A expressão "Ta flickando" vem daí.
        # Aconteceu cmg enquanto carregava os assets para o background do Leve_1, esqueci o comando flip()

        return None

