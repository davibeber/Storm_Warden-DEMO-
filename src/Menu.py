import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from src.CONST import MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self,window):
        self.window=window
        self.surf= pygame.image.load("./assets/backgrounds/PRE_ORIG_SIZE.png")
        self.rect= self.surf.get_rect(left=0,top=0)

    def run(self,):
        pygame.mixer_music.load("./assets/soundtrack/oliver siimon - epic cinematic background music 2 a major 85.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Primeiro o comando do background para dps por o texto
            self.menu_text(50,"Storm Warden",(255,174,0), ((576/2), 70))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20,MENU_OPTION[i],(COLOR_WHITE), ((576/2), 200+30 * i))

            pygame.display.flip()

            # Check for all events / traduzir isso dps
            for events in pygame.event.get():
                # Entender melhor isso
                if events.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    # Todo texto acaba virando uma imagem

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

