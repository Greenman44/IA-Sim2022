from map.Cell import Cell


class Animal:
    def __init__(self, pos_x, pos_y):
        self.data = {"vision" : 3, "strength" : 1, "mobility" : 2, "stamina" : 2, "initial_stm" : 2}
        self.pos_x = pos_x
        self.pos_y = pos_y

    def get_perception(self):
        pass
    
    def Move(self, path: list[tuple(int,int)]):
        # TODO: Walk the path and update the values for the animal
        pass
    def __getattr__(self, attr):
        try:
            return self.data[attr]
        except KeyError:
            raise AttributeError

    def __getitem__(self, key):
        try:
            return self.__getattr__(key)
        except:
            raise KeyError

    def __setattr__(self, attr, value):
        self.data[attr] = value

    def Move(self):
        pass

    def Recovery(self):
        # TODO: Recovery the stamina if the agente pass his turn or if he ate in his turn
        self.stamina+=self.initial_stm - self.stamina





