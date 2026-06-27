import pygame
from src.Background import Background
from src.CONST import WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_image(sheet, frame, width, height, scale):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        return image

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            # --- GUI (Botões) ---
            case "Pause_BTN.png":
                caminho = "./assets/GUI/Pause_BTN.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "resume":
                caminho = "./assets/GUI/resume.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "resume_hover":
                caminho = "./assets/GUI/resume_hover.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "menu":
                caminho = "./assets/GUI/menu.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "menu_hover":
                caminho = "./assets/GUI/menu_hover.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "quit":
                caminho = "./assets/GUI/quit.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            case "quit_hover":
                caminho = "./assets/GUI/quit_hover.png"
                sprite = pygame.image.load(caminho).convert_alpha()
                btn_obj = Background(caminho, (0, 0))
                btn_obj.surf = sprite
                btn_obj.rect = sprite.get_rect()
                return btn_obj

            # --- Cenário ---
            case "Level1Bg":
                list_bg = []
                for i in range(4):
                    caminho_real = f"./assets/backgrounds/Level_1/Level1Bg{i}.png"
                    for copia in range(6):
                        pos_x_inicial = copia * WIN_WIDTH
                        bg_obj = Background(caminho_real, (pos_x_inicial, 0))
                        bg_obj.name = f"Level1Bg{i}"
                        list_bg.append(bg_obj)
                return list_bg

            case "Level1Pfr":
                list_pfr = []
                plataforma = f"./assets/plataformer/Level1Pfr0.png"
                for j in range(20):
                    list_pfr.append(Background(plataforma, (j * 128, 265)))
                return list_pfr

            # --- Personagem ---
            case "idle":
                list_anim = []
                caminho = "./assets/characters/Knight_1/idle.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(4):
                    surf = EntityFactory.get_image(sheet, x, 128, 128, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim

            case "run":
                list_anim = []
                caminho = "./assets/characters/Knight_1/run.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(7):
                    surf = EntityFactory.get_image(sheet, x, 128, 128, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim

            case "jump":
                list_anim = []
                caminho = "./assets/characters/Knight_1/jump.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(6):
                    surf = EntityFactory.get_image(sheet, x, 128, 128, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim

            case "defend":
                list_anim = []
                caminho = "./assets/characters/Knight_1/defend.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(5):
                    surf = EntityFactory.get_image(sheet, x, 128, 128, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim

            case "attack_1":
                list_anim = []
                caminho = "./assets/characters/Knight_1/attack_1.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(5):
                    surf = EntityFactory.get_image(sheet, x, 128, 128, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim
            case "hurt":
                list_anim = []
                caminho = f"./assets/characters/knight_1/hurt.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(2):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim
            case "dead":
                list_anim = []
                caminho = f"./assets/characters/knight_1/dead.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(6):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(1, 146))
                    list_anim.append(obj)
                return list_anim

            # --- Mobs ---
            case "orc_idle":
                list_anim = []
                caminho = "./assets/mobs/orc_warrior/orc_idle.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(5):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(0, 0))
                    list_anim.append(obj)
                return list_anim

            case "orc_walk":
                list_anim = []
                caminho = "./assets/mobs/orc_warrior/orc_walk.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(7):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(0, 0))
                    list_anim.append(obj)
                return list_anim

            case "orc_attack_1":
                list_anim = []
                caminho = "./assets/mobs/orc_warrior/orc_attack_1.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(4):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(0, 0))
                    list_anim.append(obj)
                return list_anim
            case "orc_hurt":
                list_anim = []
                caminho = f"./assets/mobs/orc_warrior/orc_hurt.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(2):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(0, 0))
                    list_anim.append(obj)
                return list_anim
            case "orc_dead":
                list_anim = []
                caminho = f"./assets/mobs/orc_warrior/orc_dead.png"
                sheet = pygame.image.load(caminho).convert_alpha()
                for x in range(4):
                    surf = EntityFactory.get_image(sheet, x, 96, 96, 1)
                    obj = Background(caminho, (0, 0))
                    obj.surf = surf
                    obj.rect = surf.get_rect(topleft=(0, 0))
                    list_anim.append(obj)
                return list_anim

        return None