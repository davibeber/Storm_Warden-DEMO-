import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.CONST import MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self,window):
        self.window=window
        self.surf= pygame.image.load("./assets/backgrounds/PRE_ORIG_SIZE.png").convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        # Surface (Superficie) = imagem, visual
        #rect (retangulo) = Caixa invisivel que envolve a imagem (a posição fisica).

        # rect seria formado pelo plano cartesiano, X e Y, mas representados ao contrário,
        # com cordenadas positivas começando do canto superior esquerdo e aumentando pela tela,
        # usando eixos negativos para fazer objetos sumirem ou aparecerem


        # get (do inglês, pegar/obter) = usado quando uma função simplesmente serve para
        # buscar, extrair ou ler informação dentro do objeto, ela começa com "get";

        # O Python não adota a escrita camelCase, então usa underscore ("_") por regra visual

    def run(self, dt=0):

        menu_option = 0
        # Pq isso aqui funcionou?

        pygame.mixer_music.load("./assets/soundtrack/oliver siimon - epic cinematic background music 2 a major 85.mp3")
        pygame.mixer_music.play(-1)

        # pacote/biblioteca;submodulo da biblioteca; metodo ou função
        # Mas pq -1? representa o infinito ou "por tempo indeterminado" quando se fala de repetições
        # Quando escolhe numeros a partir do zero, indica quantas vezes vai tocar, emtão há limites:
        # 0 = 1 vez; 1 = 2 vezes; ...


        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # O que é blit?
            # Abreviação do termo BitLit Image Transfer (Transferência de Imagem por Blocos de Bits).
            # no dia a dia do desenvolvimento, blit significa "desenhar", "carimbar" ou "copiar"
            # os pixels de uma imagem em cima de outra tela.

            self.menu_text(50,"Storm Warden",(255,174,0), ((576/2), 70))
            # Primeiro o comando do background para dps por o texto


            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20,MENU_OPTION[i],(COLOR_YELLOW), ((576/2), 200+30 * i))

                else:
                    self.menu_text(20,MENU_OPTION[i],(COLOR_WHITE), ((576/2), 200+30 * i))
            pygame.display.flip()





            # Check for all events / Confira todos os eventos
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame / Alt + F4 tbm funciona

                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            # len = length(comprimento)
                            # no caso, o tamanho da tupla da CONST

                            # Só está calculado com (-1) pra evitar buscar uma opção que não existe
                            # Como len = 3 (0,1,2) --> 3-1=2 considera como casa limite
                            menu_option += 1
                            # Desce/soma 1 até o limite
                        else:
                            menu_option = 0 # aqui volta para "JOGAR"
                    if events.key == pygame.K_UP: # A mesma coisa, porém ao contrário
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                            # len() seria o alcance, como tem 3 opções (0,1,2)
                            # fica --> menu_option = 3-1= 2 --< retorna para "SAIR"
                    if events.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]
                    # Acho q não vou usar esse comando do enter, trocar ou tirar dps






    # o texto acaba virando uma imagem


    # Uma função pega em videoaula para uso provisório
    # Com o decorrer dos estudos, talvez eu altere para algo mais autoral
    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # tuple = tuplas

        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

