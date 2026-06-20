from src.Background import Background

# from src.Player import Player
# from src.Enemy import Enemy

class EntityFactory:

    # Isola a criação dos objetos.
    # É um intermediario, encontrando o que cada classe precisa nas pastas



    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "Level1Bg": # estava sem ideias então usei a videoaula como ponto de partida
                list_bg = [] # bg = background
                for i in range(4):
                    caminho_real = f"./assets/backgrounds/Level_1/Level1Bg{i}.png"
                    # list_bg.append(Background(caminho_real, position))
                    # list_bg.append(Background(f"Level1Bg{i}", (0,0)))
                    list_bg.append(Background(caminho_real, (0,0)))
                return list_bg
            case "Level1Pfr":
                list_pfr = []
                for i in range(1):
                    plataforma = f"./assets/plataformer/Level1Pfr0.png"



                for j in range(20):
                    pos_x = j * 128  # Multiplica o índice atual pelo tamanho do bloco (0, 128, 256...)
                    pos_y = 265  # Altura fixa do chão na tela
                    # list_pfr.append(Background(plataforma, (0,265)))
                    list_pfr.append(Background(plataforma, (pos_x, pos_y)))
                return list_pfr





                # pq match e não swtich case? qual a diferença?
                # Não há literalmente um switch (trocar) case no python, tal funcionalidade só foi
                # adicionada em 2021, o match (combinar) case, um switch 2.0 que interpreta coisas alem
                # de números e não precisa de "break".

                # list_bg=[] é uma lista ou dicionario? pq vazia?
                # lista vazia. Dicionario usaria {}
                # carregar as imagens para backgrounds. Mas com um detalhe técnico bem importante:
                # a lista não guarda as imagens puras (.png),
                # ela guarda os objetos da classe Background, e cada um desses
                # objetos carrega a sua respectiva imagem lá dentro.
                # Para o efeito Parallax do seu jogo funcionar, você precisa de
                # movimento independente. Se você usasse uma única imagem gigante para
                # o fundo, tudo se moveria na mesma velocidade, parecendo um cenário
                # estático e travado.


                # range() sempre me confunde, é sobre alcance mas
                # não consigo adaptar a explicação para o uso de mais de um arquivo

                # Por algum motivo, list_bg.append() está pegando ... e adicionando algo
                # que está usando a classe background(), acho que estaria usando o construtor dela
                # se __init__ é construtor, prosseguimos, está dando o nome e a posição em tuple.
                # usar o construtor dentro da função eu entendi, embora não tenho criatividade para
                # fazer na pratica, mas não entendo o {i}, seira pra usar a qnt de arquivos (4) dentro
                # da pasta?
                # o range() nunca entra em pasta, ele automatiza o processo evitando em criar scripts um para
                # cada arquivo e faz um "puzzle" juntando o numero que foi até o limite do "i" para encaixar com
                # o nome do arquivo e pega-lo, a mensagem é guardada pelo background e dps é enviada para entity



                # vai ter que me explicar mais o case_: return [], se é uma proteção
                # quero saber pq essa escrita estranha