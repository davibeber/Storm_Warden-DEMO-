import pygame
import self


class Player:
    def __init__(self, window, name:str):
        self.rect = None
        self.window = window
        self.window = window
        self.name = name
        self.Player_list: list=[]


        # import temporário pois tive que resolver um loop
        from src.EntityFactory import EntityFactory

        self.Player_list.extend(EntityFactory.get_entity("Idle"))

    # Talvez a adição disso seja um erro técnico, apagar quando não for relevante para a conclusão
    def update(self,):
        pass

    def move(self, ):



        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.y < 150:
            self.rect.centery -= 1
        if pressed_key[pygame.K_DOWN] and self.rect.y > 206:
            self.rect.centery += 1
        if pressed_key[pygame.K_LEFT] and self.rect.x > 1:
            self.rect.centerx -= 1
        if pressed_key[pygame.K_RIGHT] and self.rect.x < 150:
            self.rect.centerx += 1

        # Pq não comentou com elif? pq vai entender que só pode pressionar uma de cada vez e não tudo ao mesmo tempo



        for ent in self.Player_list:
            self.window.blit(source=ent.surf, dest=ent.rect)
        return None

