

class Player:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.Player_list: list=[]


        # import temporário pois tive que resolver um loop
        from src.EntityFactory import EntityFactory

        self.Player_list.extend(EntityFactory.get_entity("Idle"))
        pass

    def update(self,):
        pass

    def move(self,):


        for ent in self.Player_list:
            self.window.blit(source=ent.surf, dest=ent.rect)
        return None

