from animals.Animal import *

class Predator(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
    
    def get_perception(self, map):
        pass
    
    def Move(self,map,play):
        return super().Move(map,play)
    
    def Recovery(self):
        return super().Recovery()

class Lion(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 3
        self.mobility = 5
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 6
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Wolf(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 2
        self.mobility = 8
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 8
    def Move(self,map,play):
        return super().Move(map,play)

    def Recovery(self):
        return super().Recovery()

class Tiger(Predator):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.strength = 3
        self.mobility = 5
        self.stamina = 7
        self.initial_stm = 7
    def Move(self, map, play):
        return super().Move(map, play)
    def Recovery(self):
        return super().Recovery()
