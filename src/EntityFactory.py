import pygame

from src.Background import Background
from src.CONST import WIN_WIDTH


# from src.Player import Player
# from src.Enemy import Enemy

class EntityFactory:

    # Isola a criação dos objetos.
    # É um intermediario, encontrando o que cada classe precisa nas pastas

    @staticmethod
    def get_image(sheet, frame, width, height, scale):
        # Cria uma superfície transparente para o tamanho de um único frame
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        # SCARLPHA? esquisito isso. troco?


        # A matemática que você descobriu: corta o frame correto movendo o X
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))

        # Aplica a escala (o multiplicador de tamanho)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image





    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case "Level1Bg": # estava sem ideias então usei a videoaula como ponto de partida
                list_bg = [] # bg = background
                for i in range(4):
                    caminho_real = f"./assets/backgrounds/Level_1/Level1Bg{i}.png"
                    # list_bg.append(Background(f"Level1Bg{i}", (0,0)))
                    list_bg.append(Background(caminho_real, (0,0)))
                    # list_bg.append(Background(caminho_real, (WIN_WIDTH, 0)))
                return list_bg


            case "Level1Pfr":
                list_pfr = []
                for i in range(1):
                    plataforma = f"./assets/plataformer/Level1Pfr{i}.png"

                for j in range(20):
                    pos_x = j * 128  # Multiplica o índice atual pelo tamanho do bloco (0, 128, 256...)
                    pos_y = 265  # Altura fixa do chão na tela
                    # list_pfr.append(Background(plataforma, (0,265)))
                    list_pfr.append(Background(plataforma, (pos_x, pos_y)))
                return list_pfr

            # case "Idle": # Não seria melhor mudar para algo mais genérico como "case knight"?
            # e dps disso, criar funções que descrevem, "enquanto kinght parado ou sem resposta do teclado = idle"?




            # Se futuramente você tiver "Run" ou "Attack", pode gerenciar com ifs aqui dentro
            # Vamos tentar montar uma ligação desse if com o player para identificar quando não houver
            # resposta do teclado

            case "idle":
                list_idle = []
                caminho_sheet = "./assets/characters/Knight_1/idle.png"

                # 1. Carrega a folha de sprites inteira na memória
                sprite_sheet = pygame.image.load(caminho_sheet).convert_alpha()

                # 2. Faz um loop para cortar cada um dos 4 frames da animação
                for x in range(4):
                    # Corta o frame (largura 44, altura 65, escala aumentada em 3x)
                    frame_surf = EntityFactory.get_image(sprite_sheet, x, 128, 128, 1)

                    # Cria o objeto usando a classe Background para manter o padrão que você usa
                    objeto_frame = Background(caminho_sheet, (0, 0))

                    # Substitui a imagem estática completa pelo frame cortado e ajusta o retângulo físico dele
                    objeto_frame.surf = frame_surf
                    objeto_frame.rect = frame_surf.get_rect(topleft=(1,146))
                    # (200, 265 - 256)
                    # 128 * 2 (escala) = 256px de altura → 265 - 256 = 9
                    # objeto_frame.rect = frame_surf.get_rect(topleft=(200, 9))

                    # Guarda o frame cortado na lista
                    list_idle.append(objeto_frame)

                # Retorna a lista contendo os 4 objetos de frame prontinhos
                return list_idle
        return None

