from map.Cell import Cell


class Animal:
    def __init__(self, pos_x, pos_y):
        self.strength = 1
        self.mobility = 1
        self.vision = 2
        self.stamina = 2
        self.initial_stm = 2
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_perception(self):
        pass
    
    def Move(self, path: list[tuple(int,int)]):
        # TODO: Walk the path and update the values for the animal
        pass

    def Recovery(self):
        # TODO: Recovery the stamina if the agente pass his turn or if he ate in his turn
        self.stamina+=self.initial_stm - self.stamina





