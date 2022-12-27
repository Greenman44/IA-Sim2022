from animals.Animal import *

class Prey(Animal):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
    
    def get_perception(self, map):
        pass

    def Move(self,map,play):
        return super().Move(map,play)

    def Recovery(self):
        return super().Recovery()

class Deer(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.mobility = 7
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 9
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Hare(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.mobility = 6
        self.stamina = 4
        self.initial_stm = 4
        self.vision = 4
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Zebra(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.mobility = 4
        self.stamina = 6
        self.initial_stm = 6
        self.vision = 5
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()

class Monkey(Prey):
    def __init__(self,posx,posy):
        super().__init__(posx,posy)
        self.mobility = 4
        self.stamina = 5
        self.initial_stm = 5
        self.vision = 6
    def Move(self,map,play):
        return super().Move(map,play)
    def Recovery(self):
        return super().Recovery()